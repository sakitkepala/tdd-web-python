import os
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

MAX_TUNGGU = 10


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

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
                time.sleep(.25)

    def menunggu(self, fn):
        time_mulai = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - time_mulai > MAX_TUNGGU:
                    raise e
                time.sleep(.25)
