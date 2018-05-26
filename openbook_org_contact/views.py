# Create your views here.
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, PermissionDenied
from django.conf import settings
from ipware import get_client_ip

from openbook_org_contact.responses import ApiMessageResponse
from openbook_org_contact.serializers import ContactSerializer
import requests
import logging

logger = logging.getLogger(__name__)

OPENBOOK_CONTACT_FORM_MAIL = settings.OPENBOOK_CONTACT_FORM_MAIL
GOOGLE_RECAPTCHA_SECRET_KEY = settings.GOOGLE_RECAPTCHA_SECRET_KEY

class Contact(APIView):
    serializer_class = ContactSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.on_valid_request_data(request, serializer.validated_data)

    def on_valid_request_data(self, request, data):

        if not self.has_valid_captcha(request, data):
            raise PermissionDenied('Failed captcha')

        sender = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        try:
            requests.post(
                "https://api.mailgun.net/v3/mg.open-book.org/messages",
                auth=("api", settings.MAILGUN_API_KEY),
                data={"from": "Contact Form Openbook <mailgun@mg.open-book.org>",
                      'h:Reply-To': sender,
                      "to": [OPENBOOK_CONTACT_FORM_MAIL],
                      "subject": subject,
                      "text": message})
        except requests.exceptions.RequestException as e:
            logger.exception('Contact failed:', e)
            raise APIException('The server could not deliver your message')
        return ApiMessageResponse('Message will be delivered. Thank you.')

    def has_valid_captcha(self, request, data):
        ip, is_routable = get_client_ip(request)
        if not ip:
            raise PermissionDenied('No IP address could be determined for sender')
        else:
            if is_routable or not settings.IS_PRODUCTION_ENVIRONMENT:
                try:
                    captcha = data.get('captcha')
                    captcha_response = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
                        'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
                        'response': captcha,
                        'remoteip': ip
                    })
                except requests.exceptions.RequestException as e:
                    raise APIException('Could verify captcha with google')

                captcha_data = captcha_response.json()

                return captcha_data.get('success')
            else:
                raise PermissionDenied('No public IP address could be determined for sender')
