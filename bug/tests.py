from django.test import TestCase, Client
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User as LoginUser
from django.urls import reverse


from bug.models import User, EmailAddress

class ModelAdminTests(TestCase):

    def setUp(self):
        self.client = Client()
        LoginUser.objects.create_superuser('test', password='test')
        self.user = User.objects.create(
            name='User',
        )
        self.email1 = EmailAddress.objects.create(address='user@example.com', user=self.user)
        self.email2 = EmailAddress.objects.create(address='user2@example.com', user=self.user)
        self.client.login(username='test', password='test')

    def test_delete_email(self):
        url = reverse(f'admin:{self.user._meta.app_label}_{self.user._meta.model_name}_change', args=[self.user.id])
        page = self.client.get(url)
        response = self.client.post(url,
            data={
                'name': 'User',
                'emails-TOTAL_FORMS': '5',
                'emails-INITIAL_FORMS': '2',
                'emails-1-DELETE': 'on',
                'emails-MIN_NUM_FORMS': '0',
                'emails-MAX_NUM_FORMS': '1000',
                'emails-0-user': '1',
                'emails-0-address': 'roman2@gmail.com',
                'emails-1-user': '1',
                'emails-1-address': 'roman@gmail.com',
                'emails-1-DELETE': 'on',
                'emails-2-user': '1',
                'emails-2-address': '',
                'emails-3-user': '1',
                'emails-3-address': '',
                'emails-4-user': '1',
                'emails-4-address': '',
                'emails-__prefix__-user': '1',
                'emails-__prefix__-address': '',
                '_save': 'Save',
            })
