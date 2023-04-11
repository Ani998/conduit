#IMPORTOK
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import csv


class TestConduit(object):
    def setup_method(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "http://localhost:1667/"
        self.browser.get(URL)
        self.browser.maximize_window()

    def teardown_method(self):
        self.browser.quit()

#ATC_001 - ADATKEZELÉSI NYILATKOZAT HASZNÁLATA (Sütik elfogadása)
    def test_accept_cookies(self):
        accept_btn = self.browser.find_element(By.XPATH, "//button[@class= 'cookie__bar__buttons__button cookie__bar__buttons__button--accept']")
        accept_btn.click()
        cookie_accept = self.browser.get_cookie("vue-cookie-accept-decline-cookie-policy-panel")

        assert cookie_accept["value"] == "accept"
        time.sleep(2)

# ATC_002 - REGISZTRÁCIÓ

    def registration(self):
        self.


# ATC_003 - BEJELENTKEZÉS

# ATC_004 - ADATOK LISTÁZÁSA
# ATC_005 - TÖBB OLDALAS LISTA BEJÁRÁSA
# ATC_006 - ÚJ ADAT BEVITEL (Bejegyzés létrehozása)
# ATC_007 - ISMÉTELT ÉS SOROZATOS ADATBEVITEL ADATFORRÁSBÓL (Commentek létrehozása)
# ATC_008 - MEGLÉVŐ ADAT MÓDOSÍTÁS (Profiladatok módosítása)
# ATC_009 - ADAT VAGY ADATOK TÖRLÉSE (Bejegyzés törlése)
# ATC_010 - ADATOK LEMENTÉSE FELÜLETRŐL (Tagek mentése)
# ATC_011 - KIJELENTKEZÉS


