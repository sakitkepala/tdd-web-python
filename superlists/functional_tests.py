from selenium import webdriver
import unittest

class TestVisitorBaru(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_bisa_memulai_list_dan_tarik_lagi_nantinya(self):
        # MJ baru saja dengar tentang app todo online
        # yang oke punya. Dia lalu cek websitenya.
        self.browser.get('http://localhost:8000')

        # Dia memperhatikan title dan header halamannya
        # menyebut todo list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Selesaikan testnya!')

        # Dia diajak untuk langsung memasukkan satu item todo

        # Dia mengetikkan "Beli bulu merak" ke dalam text box
        # (hobi MJ mengikat umpan pancing pemikat ikan)

        # Ketika pencet enter, halaman terupdate, dan sekarang
        # halamannya menampilkan list "1: Beli bulu merak"
        # sebagai salah satu item yang ada di list todo

        # Masih ada text box yang ajak dia isikan item lagi. Dia
        # masukkan "Pakai bulu merak untuk membuat umpan pancing
        # pemikat" (MJ memang agak metodis).

        # Halamannya terupdate lagi, dan sekarang menampilkan
        # kedua item dalam listnya.

        # MJ bertanya-tanya apakah websitenya akan mengingat
        # list yang dia buat. Lalu dia lihat kalau situsnya
        # memunculkan URL unik untuknya -- ada semacam teks
        # penjelas untuk efek itu.

        # Dia kunjungi link itu - todo list buatannya masih di situ.

        # Puas, dia balik tidur lagi.

        # browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
