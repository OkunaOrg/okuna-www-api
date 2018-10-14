from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from openbook_org_contact.views import Contact
from unittest import mock
from unittest.mock import patch
import json


class TestContactView(APITestCase):

    contact_url = reverse('contact')

    def test_contact_form_successfully_submitted(self):
        with mock.patch.object(Contact, 'has_valid_captcha', return_value=True):
            class_instance = Contact()
            self.assertTrue(class_instance.has_valid_captcha(request={}, data={}))
            contact_data = {
                "email": "testing@test.com",
                "captcha": "myRandomCaptcha",
                "subject": "mySubject",
                "message": "myMessageThatIsAtleast10Chars"
            }
            response = self.client.post(self.contact_url, data=json.dumps(contact_data),
                                        content_type='application/json')
            self.assertTrue(response.status_code, status.HTTP_200_OK)
            self.assertTrue(response.json()["message"], "Message will be delivered. Thank you.")

    def test_contact_form_missing_captcha_error(self):
        with mock.patch.object(Contact, 'has_valid_captcha', return_value=True):
            class_instance = Contact()
            self.assertTrue(class_instance.has_valid_captcha(request={}, data={}))
            contact_data = {
                "email": "testing@test.com",
                "subject": "mySubject",
                "message": "myMessageThatIsAtLeast10Chars"
            }
            response = self.client.post(self.contact_url, data=json.dumps(contact_data),
                                        content_type='application/json')

            self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertTrue(response.json()["captcha"], "This field is required.")


class MockMailChimpListMembers:

    def all(self, id, get_all):
        resp = {"members": ["myemail@mydomain.com", "myemail2@mydomain.com", "myemail3@mydomain.com"]}
        return resp

    def __init__(self, *args, **kwargs):
        super(MockMailChimpListMembers, self).__init__(*args, **kwargs)


class MockMailChimpLists:

    members = MockMailChimpListMembers()

    def __init__(self, *args, **kwargs):
        super(MockMailChimpLists, self).__init__(*args, **kwargs)

    def update_members(self, list_id=None, data=None):
        resp = {"email": "myemail@mydomain.com"}
        return json.dumps(resp)


class MockMailChimp:

    lists = MockMailChimpLists()

    def __init__(self, *args, **kwargs):
        super(MockMailChimp, self).__init__(*args, **kwargs)


class TestWaitlistSubscribeView(APITestCase):

    subscribe_url = reverse('waitlist_subscribe')

    def test_subscribe_successfully(self):

        subscribe_data = {
            "email": "myemail@mydomain.com"
        }
        with patch('openbook_org_contact.views.MailChimp', return_value=MockMailChimp):
            response = self.client.post(self.subscribe_url, data=json.dumps(subscribe_data),
                                    content_type='application/json')
            self.assertTrue(response.status_code, status.HTTP_200_OK)
            self.assertTrue(response.content.count, 3)

