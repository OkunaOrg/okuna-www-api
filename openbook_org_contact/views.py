# Create your views here.
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, PermissionDenied
from django.conf import settings

from openbook_org_contact.responses import ApiMessageResponse
from openbook_org_contact.serializers import ContactSerializer
import requests
import logging

logger = logging.getLogger(__name__)

OPENBOOK_CONTACT_FORM_MAIL = settings.OPENBOOK_CONTACT_FORM_MAIL

class Contact(APIView):
    serializer_class = ContactSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.on_valid_request_data(request, serializer.validated_data)

    def on_valid_request_data(self, request, data):
        if not self.has_valid_recaptcha(request, data):
            raise PermissionDenied('Failed recaptcha')

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

    def has_valid_recaptcha(self, request, data):
        return True
