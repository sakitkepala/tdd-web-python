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
        self.client.post('/', data={'item_text': 'Satu item list baru'})

        self.assertEqual(Item.objects.count(), 1)
        item_baru = Item.objects.first()
        self.assertEqual(item_baru.text, 'Satu item list baru')

    def test_redirect_setelah_POST(self):
        response = self.client.post('/', data={'item_text': 'Satu item list baru'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_menampilkan_semua_item_list(self):
        Item.objects.create(text='Semacam item 1')
        Item.objects.create(text='Semacam item 2')

        response = self.client.get('/')

        self.assertIn('Semacam item 1', response.content.decode())
        self.assertIn('Semacam item 2', response.content.decode())

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

    def test_cuma_akan_simpan_item_saat_diperlukan(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
