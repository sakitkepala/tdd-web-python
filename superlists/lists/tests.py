from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


class TestHomePage(TestCase):

    def test_url_root_resolve_ke_view_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
