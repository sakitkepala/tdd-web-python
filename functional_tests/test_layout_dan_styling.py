from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time


class TestLayoutDanStyling(FunctionalTest):

    def test_layout_dan_styling(self):
        # MJ ke halaman home
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        time.sleep(.1) # browser nge-close-nya kecepetan sebelum windownya sempat ke-resize lebarnya, di-delay sebentar biar sempat ke-resize dulu

        # Dia lihat box inputnya ada di tengah dengan apik
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # Dia bikin list baru dan lihat inputnya di sana juga
        # ada di tengah dengan apik
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.tunggu_row_di_tabel_list('1: testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
