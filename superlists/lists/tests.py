from django.test import TestCase
from lists.models import Item, List


class TestHomePage(TestCase):

    def test_pakai_template_home(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')


class TestListBaru(TestCase):

    def test_bisa_simpan_request_POST(self):
        self.client.post('/lists/baru', data={'item_text': 'Satu item list baru'})

        self.assertEqual(Item.objects.count(), 1)
        item_baru = Item.objects.first()
        self.assertEqual(item_baru.text, 'Satu item list baru')

    def test_redirect_setelah_POST(self):
        response = self.client.post('/lists/baru', data={'item_text': 'Satu item list baru'})

        self.assertRedirects(response, '/lists/satu-satunya-list-di-dunia/')


class TestListView(TestCase):

    def test_pakai_template_list(self):
        response = self.client.get('/lists/satu-satunya-list-di-dunia/')

        self.assertTemplateUsed(response, 'list.html')

    def test_menampilkan_semua_item(self):
        list_ = List.objects.create()
        Item.objects.create(text='Semacam item 1', list=list_)
        Item.objects.create(text='Semacam item 2', list=list_)

        response = self.client.get('/lists/satu-satunya-list-di-dunia/')

        self.assertContains(response, 'Semacam item 1')
        self.assertContains(response, 'Semacam item 2')


class TestListDanItemModel(TestCase):

    def test_simpan_dan_tarik_item(self):
        list_ = List()
        list_.save()

        item_pertama = Item()
        item_pertama.text = 'Item list yang (paling) pertama'
        item_pertama.list = list_
        item_pertama.save()

        item_kedua = Item()
        item_kedua.text = 'Item yang kedua'
        item_kedua.list = list_
        item_kedua.save()

        list_tersimpan = List.objects.first()
        self.assertEqual(list_tersimpan, list_)

        item_tersimpan = Item.objects.all()
        self.assertEqual(item_tersimpan.count(), 2)

        item_tersimpan_pertama = item_tersimpan[0]
        item_tersimpan_kedua = item_tersimpan[1]
        self.assertEqual(item_tersimpan_pertama.text, 'Item list yang (paling) pertama')
        self.assertEqual(item_tersimpan_pertama.list, list_)
        self.assertEqual(item_tersimpan_kedua.text, 'Item yang kedua')
        self.assertEqual(item_tersimpan_kedua.list, list_)
