# IMPORTOK
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from user_data import user
from import_functions import login, registration, new_article
from articles import arcticle1
import allure
import csv


# SETUP ÉS TEARDOWN
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
    @allure.title('ADATKEZELÉSI NYILATKOZAT HASZNÁLATA')
    def test_accept_cookies(self):
        accept_btn = self.browser.find_element(By.XPATH,
                                               "//button[@class= 'cookie__bar__buttons__button cookie__bar__buttons__button--accept']")
        accept_btn.click()
        cookie_accepted = self.browser.get_cookie("vue-cookie-accept-decline-cookie-policy-panel")
        assert cookie_accepted["value"] == "accept"

    # ATC002 - REGISZTRÁCIÓ (Regisztráció helyes adatokkal)
    @allure.title('REGISZTRÁCIÓ')
    def test_registration(self):
        registration(self.browser)

        registration_msg = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
        assert registration_msg.text == "Welcome!"

    # ATC003 - BEJELENTKEZÉS (Bejelentkezés helyes adatokkal)
    @allure.title('BEJELENTKEZÉS')
    def test_login(self):
        login(self.browser)

        my_feed = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link router-link-exact-active active"]')))
        assert my_feed.is_displayed()

    # ATC004 - ADATOK LISTÁZÁSA (Lorem taggel rendlkező bejegyzések listázása)
    @allure.title('ADATOK LISTÁZÁSA')
    def test_listing(self):
        login(self.browser)

        lorem_tag = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div/div/a[@href="#/tag/lorem"]')))
        lorem_tag.click()
        articles = WebDriverWait(self.browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="preview-link"]/h1')))
        assert len(articles) != 0

    # ATC005 - TÖBB OLDALAS LISTA BEJÁRÁSA
    @allure.title('TÖBB OLDALAS LISTA BEJÁRÁSA')
    def test_list_pages(self):
        login(self.browser)

        pages = WebDriverWait(self.browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="page-link"]')))

        for page in pages:
            page.click()
            first_page = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/div/div/nav/ul/li[1]/a')))
            second_page = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/div/div/nav/ul/li[2]/a')))
            assert first_page.text != second_page.text

    # ATC006 - ÚJ ADAT BEVITEL (Bejegyzés létrehozása)
    @allure.title('ÚJ ADAT BEVITEL')
    def test_new_article(self):
        login(self.browser)
        new_article(self.browser)

        actual_article_title = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//h1')))
        assert actual_article_title.text == arcticle1["title"]
        # az about csak a saját profilból megnyitva látszik, a bejegyzés előnézetében nem.
        actual_text = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[1]/p')
        assert actual_text.text == arcticle1["text"]
        actual_tag = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/a')
        assert actual_tag.text == arcticle1["tag"]

    # ATC007 - ISMÉTELT ÉS SOROZATOS ADATBEVITEL ADATFORRÁSBÓL (Commentek létrehozása)
    # A címnek egyedinek kell lennie, ugyanazzal a címmel nem jelenhet meg több bejegyzés!

    @allure.title('ISMÉTELT ÉS SOROZATOS ADATBEVITEL ADATFORRÁSBÓL')
    def test_data_inputs_from_file(self):
        login(self.browser)

        with open('vizsgaremek_teszt/more_articles.csv', 'r') as data:
            datas = csv.reader(data, delimiter=',')
            next(datas)
            for i in datas:
                new_article_btn = WebDriverWait(self.browser, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//a[@href="#/editor"]')))
                new_article_btn.click()
                article_title = WebDriverWait(self.browser, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]')))
                article_about = self.browser.find_element(By.XPATH,
                                                          '//input[@placeholder="What\'s this article about?"]')
                article_text = self.browser.find_element(By.XPATH,
                                                         '//textarea[@placeholder="Write your article (in markdown)"]')
                article_tag = self.browser.find_element(By.XPATH, '//input[@placeholder="Enter tags"]')
                publish_btn = self.browser.find_element(By.XPATH,
                                                        '//button[@class="btn btn-lg pull-xs-right btn-primary"]')

                article_title.send_keys(i[0])
                article_about.send_keys(i[1])
                article_text.send_keys(i[2])
                article_tag.send_keys(i[3])
                publish_btn.click()
                time.sleep(3)
        published_article_title = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//h1')))
        assert published_article_title.text == i[0]

    # ATC008 - ADAT VAGY ADATOK TÖRLÉSE (Bejegyzés törlése)
    @allure.title('ADAT VAGY ADATOK TÖRLÉSE')
    def test_delete(self):
        login(self.browser)
        time.sleep(3)
        open_article = self.browser.find_elements(By.CSS_SELECTOR, 'h1')[1]
        open_article.click()
        comment_input = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div[1]/form/div[1]/textarea')))
        comment_input.send_keys('This comment will be gone soon hopefully...')
        post_comment_btn = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div[1]/form/div[2]/button')
        post_comment_btn.click()
        trash_icon = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/span[2]')))
        trash_icon.click()
        time.sleep(5)
        new_comment_text = self.browser.find_elements(By.CSS_SELECTOR, 'html body div#app div.article-page div.container.page div.row div.col-xs-12.col-md-8.offset-md-2')[0]
        assert new_comment_text.text != 'This comment will be gone soon hopefully...'

    # ATC09 - ADATOK LEMENTÉSE FELÜLETRŐL (Tagek mentése)
    def test_save_data(self):
        login(self.browser)

        popular_tags = WebDriverWait(self.browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div/div/a[@class="tag-pill tag-default"]')))

        tags = []
        for tag in popular_tags:
            tags.append(tag.text)
        print(tags)

        with open('tags', 'w', encoding="UTF-8") as tag_file:
            tag_file.write(str(tags))

    # ATC010 - KIJELENTKEZÉS
    @allure.title('KIJELENTKEZÉS')
    def test_log_out(self):
        login(self.browser)

        logout_btn = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//a[@active-class="active"]')))
        logout_btn.click()
        signin_btn = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="#/login"]')))
        assert signin_btn.is_displayed()

    # ATC011 - MEGLÉVŐ ADAT MÓDOSÍTÁS (Profiladatok módosítása)
    @allure.title('MEGLÉVŐ ADAT MÓDOSÍTÁS')
    def test_update_data(self):
        login(self.browser)
        setting_btn = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/nav/div/ul/li[3]/a')))
        setting_btn.click()
        new_image = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[1]/input')))
        new_image.clear()
        new_image.send_keys('https://static.productionready.io/images/smiley-cyrus.jpg')
        new_username = self.browser.find_element(By.XPATH,
                                                 '/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[2]/input')
        new_username.clear()
        new_username.send_keys('New username')
        new_bio = self.browser.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
        new_bio.clear()
        new_bio.send_keys('Ez az új bióm')
        update_btn = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/form/fieldset/button')
        update_btn.click()
        update_succes_msg = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]')))
        assert update_succes_msg.text == 'Update successful!'