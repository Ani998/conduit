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

#ATC001 - ADATKEZELÉSI NYILATKOZAT HASZNÁLATA (Sütik elfogadása)
    def test_accept_cookies(self):
        accept_btn = self.browser.find_element(By.XPATH, "//button[@class= 'cookie__bar__buttons__button cookie__bar__buttons__button--accept']")
        accept_btn.click()
        time.sleep(2)

        cookie_accepted = self.browser.get_cookie("vue-cookie-accept-decline-cookie-policy-panel")
        assert cookie_accepted["value"] == "accept"
        time.sleep(2)

# ATC002 - REGISZTRÁCIÓ
    def test_registration(self):
        sign_up_btn = self.browser.find_element(By.LINK_TEXT, 'Sign up')
        sign_up_btn.click()

        reg_username = self.browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
        reg_username.send_keys("Valami2")
        reg_email = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        reg_email.send_keys("valami2@gmail.com")
        reg_psw = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
        reg_psw.send_keys("Strukturavaltas3")
        time.sleep(2)
        reg_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        reg_btn.click()

        registration_message = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
        assert registration_message.text == "Welcome!"


# ATC003 - BEJELENTKEZÉS


# ATC_004 - ADATOK LISTÁZÁSA
# ATC_005 - TÖBB OLDALAS LISTA BEJÁRÁSA
# ATC_006 - ÚJ ADAT BEVITEL (Bejegyzés létrehozása)
# ATC_007 - ISMÉTELT ÉS SOROZATOS ADATBEVITEL ADATFORRÁSBÓL (Commentek létrehozása)
# ATC_008 - MEGLÉVŐ ADAT MÓDOSÍTÁS (Profiladatok módosítása)
# ATC_009 - ADAT VAGY ADATOK TÖRLÉSE (Bejegyzés törlése)
# ATC_010 - ADATOK LEMENTÉSE FELÜLETRŐL (Tagek mentése)
# ATC_011 - KIJELENTKEZÉS


