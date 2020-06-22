from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

MAX_TUNGGU = 10


class TestVisitorBaru(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def tunggu_row_di_tabel_list(self, teks_row):
        time_mulai = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(teks_row, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - time_mulai > MAX_TUNGGU:
                    raise e
                time.sleep(.5)

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
        self.tunggu_row_di_tabel_list('1: Beli bulu merak')

        # Masih ada text box yang ajak dia isikan item lagi. Dia
        # masukkan "Pakai bulu merak untuk membuat umpan pancing
        # pemikat" (MJ memang agak metodis).
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Pakai bulu merak untuk membuat umpan pancing pemikat')
        inputbox.send_keys(Keys.ENTER)

        # Halamannya terupdate lagi, dan sekarang menampilkan
        # kedua item dalam listnya.
        self.tunggu_row_di_tabel_list('1: Beli bulu merak')
        self.tunggu_row_di_tabel_list('2: Pakai bulu merak untuk membuat umpan pancing pemikat')

        # MJ bertanya-tanya apakah websitenya akan mengingat
        # list yang dia buat. Lalu dia lihat kalau situsnya
        # memunculkan URL unik untuknya -- ada semacam teks
        # penjelas untuk efek itu.
        self.fail('Testnya selesai!')

        # Dia kunjungi link itu - todo list buatannya masih di situ.

        # Setelah puas, dia balik tidur lagi.

    def test_banyak_user_bisa_bikin_list_di_beda_url(self):
        # MJ bikin todo list baru
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Beli bulu merak')
        inputbox.send_keys(Keys.ENTER)
        self.tunggu_row_di_tabel_list('1: Beli bulu merak')

        # Dia sadar list yang dia buat punya url unik
        url_list_mj = self.browser.current_url
        self.assertRegex(url_list_mj, '/lists/.+')

        # Sekarang seorang user baru, Belu, datang ke website

        ## Kita pakai session browser baru untuk pastikan tidak ada
        ## informasinya MJ yang masuk dari cookie dsb.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Belu datang kunjungi halaman home. Tidak ada tanda-tanda
        # dari list MJ
        self.browser.get(self.live_server_url)
        teks_halaman = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Belu bulu merak', teks_halaman)
        self.assertNotIn('untuk membuat umpan', teks_halaman)

        # Belu bikin list baru dengan mengisikan satu item baru.
        # Dia tidak setertarik MJ.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Beli susu')
        inputbox.send_keys(Keys.ENTER)
        self.tunggu_row_di_tabel_list('1: Beli susu')

        # Belu dapat url yang khusus untuk dia sendiri
        url_list_belu = self.browser.current_url
        self.assertRegex(url_list_belu, '/lists/.+')
        self.assertNotEqual(url_list_belu, url_list_mj)

        # Sekali lagi, tidak ada jejak list milik MJ
        teks_halaman = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Beli bulu merak', teks_halaman)
        self.assertIn('Beli susu', teks_halaman)

        # Setelah puas, mereka berdua balik tidur lagi masing-masing
