from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from . import views

# Test for loading views.
class HomePageView(TestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

# Below is the base class for testing
# the main view based on permissions.
class SimpleSocialBase(TestCase):
    def user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'testuser',
            password = 'password'
        )

    def super_user(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username = 'testsuperuser',
            password = 'password'
        )