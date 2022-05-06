from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# Creating Tests here


class ViewTest(TestCase):

    def test_view_returns_OK(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('APP:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index_new.html')