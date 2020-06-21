from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

from django.template.loader import render_to_string


class TestHomePage(TestCase):

    def test_pakai_template_home(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')

    def test_bisa_simpan_request_POST(self):
        response = self.client.post('/', data={'item_text': 'Satu item list baru'})

        self.assertIn('Satu item list baru', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
