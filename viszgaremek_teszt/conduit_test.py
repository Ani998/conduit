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
from user_data import user
from import_functions import login

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

# ATC001 - ADATKEZELÉSI NYILATKOZAT HASZNÁLATA (Sütik elfogadása)
    def test_accept_cookies(self):
        accept_btn = self.browser.find_element(By.XPATH, "//button[@class= 'cookie__bar__buttons__button cookie__bar__buttons__button--accept']")
        accept_btn.click()
        time.sleep(2)

        cookie_accepted = self.browser.get_cookie("vue-cookie-accept-decline-cookie-policy-panel")
        assert cookie_accepted["value"] == "accept"
        time.sleep(2)

# ATC002 - REGISZTRÁCIÓ (Regisztráció helyes adatokkal)
    def test_registration(self):
        sign_up_btn = self.browser.find_element(By.LINK_TEXT, 'Sign up')
        sign_up_btn.click()

        reg_username = self.browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
        reg_username.send_keys(user["name"])
        reg_email = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        reg_email.send_keys(user["email"])
        reg_psw = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
        reg_psw.send_keys(user["password"])

        reg_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        reg_btn.click()

        time.sleep(5)

        registration_msg = self.browser.find_element(By.XPATH, '//div[@class="swal-title"]')
        assert registration_msg.text == "Welcome!"


# ATC003 - BEJELENTKEZÉS (Bejelentkezés helyes adatokkal)
    def test_login(self):
        login_btn = self.browser.find_element(By.XPATH, '//a[@href="#/login"]')
        login_btn.click()

        login_email = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        login_email.send_keys(user["email"])
        login_psw = self.browser.find_element(By.XPATH, '//input[@placeholder = "Password"]')
        login_psw.send_keys(user["password"])

        login_btn_send = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        login_btn_send.click()

        time.sleep(7)

        my_feed = self.browser.find_element(By.XPATH, '//a[@class="nav-link router-link-exact-active active"]')
        assert my_feed.is_displayed()

# ATC004 - ADATOK LISTÁZÁSA (Adott felhasználó bejegyzéseinek listázása)


# ATC005 - TÖBB OLDALAS LISTA BEJÁRÁSA

# ATC006 - ÚJ ADAT BEVITEL (Bejegyzés létrehozása)

# ATC007 - ISMÉTELT ÉS SOROZATOS ADATBEVITEL ADATFORRÁSBÓL (Commentek létrehozása)

# ATC008 - MEGLÉVŐ ADAT MÓDOSÍTÁS (Profiladatok módosítása)
# ATC009 - ADAT VAGY ADATOK TÖRLÉSE (Bejegyzés törlése)
# ATC010 - ADATOK LEMENTÉSE FELÜLETRŐL (Tagek mentése)

# ATC011 - KIJELENTKEZÉS

    def test_log_out(self):
        login(self.browser)

        logout_btn = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@active-class="active"]')))
        logout_btn.click()

        signin_btn = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@href="#/login"]')))
        assert signin_btn.is_displayed()





