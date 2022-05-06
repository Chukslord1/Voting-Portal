from django.contrib.auth.models import User
from . models import Time
from django.test import TestCase
from django.urls import reverse

# Creating Tests here


class ViewTest(TestCase):

    def test_view_returns_OK(self):
        response = self.client.get('/')
        response2 = self.client.get('/candidates.html')
        response3 = self.client.get('/results.html')
        response4 = self.client.get('/activity.html')
        response5 = self.client.get('/login.html')
        response6 = self.client.get('/register.html')
        response7 = self.client.get('/candidate_reg')
        response8 = self.client.get('/voters-approved')

        self.assertEqual(response.status_code,200)
        self.assertEqual(response2.status_code,200)
        self.assertEqual(response3.status_code,200)
        self.assertEqual(response4.status_code,200)
        self.assertEqual(response5.status_code,200)
        self.assertEqual(response6.status_code,200)
        self.assertEqual(response7.status_code,200)
        self.assertEqual(response8.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('APP:index'))
        response2 = self.client.get(reverse('APP:create_vote'))
        response3 = self.client.get(reverse('APP:results'))
        response4 = self.client.get(reverse('APP:activity'))
        response5 = self.client.get(reverse('APP:login'))
        response6 = self.client.get(reverse('APP:register'))
        response7 = self.client.get(reverse('APP:candidate_reg'))
        response8 = self.client.get(reverse('APP:voters_approved'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index_new.html')
        self.assertEqual(response3.status_code, 200)
        self.assertTemplateUsed(response3, 'results.html')
        self.assertEqual(response4.status_code, 200)
        self.assertTemplateUsed(response4, 'activity_new.html')
        self.assertEqual(response5.status_code, 200)
        self.assertTemplateUsed(response5, 'login.html')
        self.assertEqual(response5.status_code, 200)
        self.assertTemplateUsed(response6, 'register.html')
        self.assertEqual(response7.status_code, 200)
        self.assertTemplateUsed(response7, 'candidate_reg.html')
        self.assertEqual(response8.status_code, 200)
