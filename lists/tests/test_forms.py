from django.test import TestCase

from lists.forms import ERROR_ITEM_KOSONG, FormItem


class TestFormItem(TestCase):

    def test_form_render_input_item_text(self):
        form = FormItem()
        self.assertIn('placeholder="Masukkan satu item to-do"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_validasi_form_untuk_item_kosong(self):
        form = FormItem(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'],
            [ERROR_ITEM_KOSONG]
        )
