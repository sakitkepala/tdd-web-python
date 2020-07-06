from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class TestValidasiItem(FunctionalTest):

    def test_tidak_bisa_nambah_item_kosongan(self):
        # MJ ke home lagi dan gak sengaja nge-submit item list
        # yang kosongan. Dia pencet Enter ketika box input masih
        # kosong.
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # Halaman home nge-refresh, dan ada pesan error yang
        # bilang item list itu tidak boleh kosong.
        self.menunggu(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            'Kamu gak boleh bikin item list kosong'
        ))

        # Dia tulis lagi, sekarang sudah dengan teks untuk itemnya,
        # yang sekarang jadi berhasil
        self.browser.find_element_by_id('id_new_item').send_keys('Beli susu')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.tunggu_row_di_tabel_list('1: Beli susu')

        # Karena penasaran, dia malah nyoba sengaja submit item
        # yang kosongan
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        
        # Dia nerima pesan peringatan yang sama di halaman list
        self.menunggu(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            'Kamu gak boleh bikin item list kosong'
        ))

        # Kemudian dia mengoreksi ddngan mengisinya teks
        self.browser.find_element_by_id('id_new_item').send_keys('Bikin teh')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.tunggu_row_di_tabel_list('1: Beli susu')
        self.tunggu_row_di_tabel_list('2: Bikin teh')
