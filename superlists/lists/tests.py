from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

from lists.models import Item


class TestHomePage(TestCase):

    def test_pakai_template_home(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')

    def test_bisa_simpan_request_POST(self):
        response = self.client.post('/', data={'item_text': 'Satu item list baru'})

        self.assertIn('Satu item list baru', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

class TestItemModel(TestCase):

    def test_simpan_dan_tarik_item(self):
        item_pertama = Item()
        item_pertama.text = 'Item list yang (paling) pertama'
        item_pertama.save()

        item_kedua = Item()
        item_kedua.text = 'Item yang kedua'
        item_kedua.save()

        item_tersimpan = Item.objects.all()
        self.assertEqual(item_tersimpan.count(), 2)

        item_tersimpan_pertama = item_tersimpan[0]
        item_tersimpan_kedua = item_tersimpan[1]
        self.assertEqual(item_tersimpan_pertama.text, 'Item list yang (paling) pertama')
        self.assertEqual(item_tersimpan_kedua.text, 'Item yang kedua')
