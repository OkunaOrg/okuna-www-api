from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from openbook_org_contact.views import Contact
from unittest import mock
from unittest.mock import patch
import json


class TestContactView(APITestCase):
    """
    Contact API
    """

    contact_url = reverse('contact')

    def test_contact_form_successfully_submitted(self):
        """
         Should submit valid contact info successfully
        """
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
        """
        Should return 400 with missing captcha
        """
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

    def test_contact_form_missing_email_error(self):
        """
        Should return 400 with missing email
        """
        with mock.patch.object(Contact, 'has_valid_captcha', return_value=True):
            class_instance = Contact()
            self.assertTrue(class_instance.has_valid_captcha(request={}, data={}))
            contact_data = {
                "captcha": "myRandomCaptcha",
                "subject": "mySubject",
                "message": "myMessageThatIsAtLeast10Chars"
            }
            response = self.client.post(self.contact_url, data=json.dumps(contact_data),
                                        content_type='application/json')

            self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertTrue(response.json()["email"], "This field is required.")

    def test_contact_form_missing_subject_error(self):
        """
        Should return 400 with missing subject
        """
        with mock.patch.object(Contact, 'has_valid_captcha', return_value=True):
            class_instance = Contact()
            self.assertTrue(class_instance.has_valid_captcha(request={}, data={}))
            contact_data = {
                "captcha": "myRandomCaptcha",
                "email": "testing@test.com",
                "message": "myMessageThatIsAtLeast10Chars"
            }
            response = self.client.post(self.contact_url, data=json.dumps(contact_data),
                                        content_type='application/json')

            self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertTrue(response.json()["subject"], "This field is required.")

    def test_contact_form_missing_message_error(self):
        """
        Should return 400 with missing message
        """
        with mock.patch.object(Contact, 'has_valid_captcha', return_value=True):
            class_instance = Contact()
            self.assertTrue(class_instance.has_valid_captcha(request={}, data={}))
            contact_data = {
                "captcha": "myRandomCaptcha",
                "email": "testing@test.com",
                "subject": "mySubject"
            }
            response = self.client.post(self.contact_url, data=json.dumps(contact_data),
                                        content_type='application/json')

            self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertTrue(response.json()["message"], "This field is required.")


class MockMailChimpListMembers:

    def all(self, id, status):
        resp = {"members": ["myemail@mydomain.com", "myemail2@mydomain.com", "myemail3@mydomain.com"]}
        return resp


class MockMailChimpLists:

    members = MockMailChimpListMembers()

    def update_members(self, list_id=None, data=None):
        resp = {"email": "myemail@mydomain.com"}
        return json.dumps(resp)


class MockMailChimp:

    lists = MockMailChimpLists()


class TestWaitlistSubscribeView(APITestCase):
    """
    Waitlist API
    """

    subscribe_url = reverse('waitlist_subscribe')

    def test_subscribe_successfully(self):
        """
        Should subscribe successfully to waitlist
        """

        subscribe_data = {
            "email": "myemail@mydomain.com"
        }
        with patch('openbook_org_contact.views.MailChimp', return_value=MockMailChimp):
            response = self.client.post(self.subscribe_url, data=json.dumps(subscribe_data),
                                    content_type='application/json')
            self.assertTrue(response.status_code, status.HTTP_200_OK)
            self.assertTrue(response.content.count, 3)

    def test_invalid_email(self):
        """
        Should return 400 with invalid email
        """

        subscribe_data = {
            "email": "myemai"
        }
        with patch('openbook_org_contact.views.MailChimp', return_value=MockMailChimp):
            response = self.client.post(self.subscribe_url, data=json.dumps(subscribe_data),
                                        content_type='application/json')
            self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)

