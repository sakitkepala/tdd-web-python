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

        list_baru = List.objects.first()
        self.assertRedirects(response, f'/lists/{list_baru.id}/')


class TestViewList(TestCase):

    def test_pakai_template_list(self):
        list_ = List.objects.create()

        response = self.client.get(f'/lists/{list_.id}/')

        self.assertTemplateUsed(response, 'list.html')

    def test_oper_list_yang_benar_ke_template(self):
        list_yang_lain = List.objects.create()
        list_yang_benar = List.objects.create()

        response = self.client.get(f'/lists/{list_yang_benar.id}/')

        self.assertEqual(response.context['list'], list_yang_benar)

    def test_menampilkan_cuma_item_yang_untuk_listnya(self):
        list_yang_benar = List.objects.create()
        Item.objects.create(text='Semacam item 1', list=list_yang_benar)
        Item.objects.create(text='Semacam item 2', list=list_yang_benar)

        list_lain = List.objects.create()
        Item.objects.create(text='Item list lain 1', list=list_lain)
        Item.objects.create(text='Item list lain 2', list=list_lain)

        response = self.client.get(f'/lists/{list_yang_benar.id}/')

        self.assertContains(response, 'Semacam item 1')
        self.assertContains(response, 'Semacam item 2')
        self.assertNotContains(response, 'Item list lain 1')
        self.assertNotContains(response, 'Item list lain 2')


class TestItemBaru(TestCase):

    def test_bisa_simpan_request_POST_ke_list_yang_sudah_ada(self):
        list_lain = List.objects.create()
        list_yang_benar = List.objects.create()

        self.client.post(
            f'/lists/{list_yang_benar.id}/tambah_item',
            data={'item_text': 'Item baru untuk list yang sudah ada'}
        )

        self.assertEqual(Item.objects.count(), 1)
        item_baru = Item.objects.first()
        self.assertEqual(item_baru.text, 'Item baru untuk list yang sudah ada')
        self.assertEqual(item_baru.list, list_yang_benar)

    def test_redirect_ke_view_list(self):
        list_lain = List.objects.create()
        list_yang_benar = List.objects.create()

        response = self.client.post(
            f'/lists/{list_yang_benar.id}/tambah_item',
            data={'item_text': 'Item baru untuk list yang sudah ada'}
        )

        self.assertRedirects(response, f'/lists/{list_yang_benar.id}/')
