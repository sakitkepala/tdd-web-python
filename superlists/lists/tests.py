from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

from django.template.loader import render_to_string


class TestHomePage(TestCase):

    def test_home_page_mereturn_html_yang_benar(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')
