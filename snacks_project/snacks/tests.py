from django.conf.urls import url
from django.http import response
from django.test import SimpleTestCase

# Create your tests here.

# tests creation
from django.urls import reverse

class snackTest(SimpleTestCase):
    def test_home_page(self):
        url=reverse('home')
        # generate url from name
        response =self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_about_page(self):
        url=reverse('about')
        # generate url from name
        response =self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_home_template(self):
        url=reverse('home')
        response =self.client.get(url)
        self.assertTemplateUsed(response,"home.html")
        self.assertTemplateUsed(response,"base.html")

    def test_about_template(self):
        url=reverse('about')
        response =self.client.get(url)
        self.assertTemplateUsed(response,"about.html")
        self.assertTemplateUsed(response,"base.html")





