from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TestVisitorBaru(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def cek_row_di_tabel_list(self, teks_row):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(teks_row, [row.text for row in rows])

    def test_bisa_memulai_list_dan_tarik_lagi_nantinya(self):
        # MJ baru saja dengar tentang app todo online
        # yang oke punya. Dia lalu cek websitenya.
        self.browser.get(self.live_server_url)

        # Dia memperhatikan title dan header halamannya
        # menyebut todo list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Dia diajak untuk langsung memasukkan satu item todo
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Masukkan satu item to-do'
        )

        # Dia mengetikkan "Beli bulu merak" ke dalam text box
        # (hobi MJ mengikat umpan pancing pemikat ikan)
        inputbox.send_keys('Beli bulu merak')

        # Ketika pencet enter, halaman terupdate, dan sekarang
        # halamannya menampilkan list "1: Beli bulu merak"
        # sebagai salah satu item yang ada di list todo
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.cek_row_di_tabel_list('1: Beli bulu merak')

        # Masih ada text box yang ajak dia isikan item lagi. Dia
        # masukkan "Pakai bulu merak untuk membuat umpan pancing
        # pemikat" (MJ memang agak metodis).
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Pakai bulu merak untuk membuat umpan pancing pemikat')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Halamannya terupdate lagi, dan sekarang menampilkan
        # kedua item dalam listnya.
        self.cek_row_di_tabel_list('1: Beli bulu merak')
        self.cek_row_di_tabel_list('2: Pakai bulu merak untuk membuat umpan pancing pemikat')

        # MJ bertanya-tanya apakah websitenya akan mengingat
        # list yang dia buat. Lalu dia lihat kalau situsnya
        # memunculkan URL unik untuknya -- ada semacam teks
        # penjelas untuk efek itu.
        self.fail('Testnya selesai!')

        # Dia kunjungi link itu - todo list buatannya masih di situ.

        # Puas, dia balik tidur lagi.
