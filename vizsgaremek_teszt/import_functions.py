from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from user_data import user
from articles import arcticle1


def registration(browser):
    sign_up_btn = browser.find_element(By.LINK_TEXT, 'Sign up')
    sign_up_btn.click()

    reg_username = browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
    reg_username.send_keys(user["name"])
    reg_email = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
    reg_email.send_keys(user["email"])
    reg_psw = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
    reg_psw.send_keys(user["password"])

    reg_btn = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    reg_btn.click()


def login(browser):
    signin_btn = browser.find_element(By.XPATH, '//a[@href="#/login"]')
    signin_btn.click()

    login_email = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
    login_email.send_keys(user["email"])
    login_psw = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
    login_psw.send_keys(user["password"])

    signin_btn = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')))
    signin_btn.click()
    time.sleep(5)


def new_article(browser):
    new_article_btn = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//a[@href="#/editor"]')))
    new_article_btn.click()
    article_title = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]')))
    article_title.send_keys(arcticle1["title"])
    article_about = browser.find_element(By.XPATH, '//input[@placeholder="What\'s this article about?"]')
    article_about.send_keys(arcticle1["about"])
    article_text = browser.find_element(By.XPATH,
                                        '//textarea[@placeholder="Write your article (in markdown)"]')
    article_text.send_keys(arcticle1["text"])
    article_tag = browser.find_element(By.XPATH, '//input[@placeholder="Enter tags"]')
    article_tag.send_keys(arcticle1["tag"])
    publish_btn = browser.find_element(By.XPATH, '//button[@class="btn btn-lg pull-xs-right btn-primary"]')
    publish_btn.click()
