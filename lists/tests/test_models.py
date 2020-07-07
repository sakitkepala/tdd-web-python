from django.test import TestCase
from lists.models import Item, List


class TestModelListDanItem(TestCase):

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
