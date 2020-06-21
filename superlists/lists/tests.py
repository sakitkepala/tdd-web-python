from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


class TestHomePage(TestCase):

    def test_url_root_resolve_ke_view_home_page(self):
        found = resolve('/')

        self.assertEqual(found.func, home_page)

    def test_home_page_mereturn_html_yang_benar(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
