from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class TestValidasiItem(FunctionalTest):

    def test_tidak_bisa_nambah_item_kosongan(self):
        # MJ ke home lagi dan gak sengaja nge-submit item list
        # yang kosongan. Dia pencet Enter ketika box input masih
        # kosong.

        # Halaman home nge-refresh, dan ada pesan error yang
        # bilang item list itu tidak boleh kosong.

        # Dia tulis lagi, sekarang sudah dengan teks untuk itemnya,
        # yang sekarang jadi berhasil

        # Karena penasaran, dia malah nyoba sengaja submit item
        # yang kosongan
        
        # Dia nerima pesan peringatan yang sama di halaman list

        self.fail('Ditulis dong.')
