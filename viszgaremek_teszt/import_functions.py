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

def registration(browser):
    sign_up_btn = browser.find_element(By.LINK_TEXT, 'Sign up')
    sign_up_btn.click()

    reg_username = browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
    reg_username.send_keys(user["name"])
    reg_email = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
    reg_email.send_keys(user["email"])
    reg_psw = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
    reg_psw.send_keys("Strukturavaltas3")

    reg_btn = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    reg_btn.click()


def login(browser):
    signin_btn = browser.find_element(By.XPATH, '//a[@href="#/login"]')
    signin_btn .click()

    login_email = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
    login_email.send_keys(user["email"])
    login_psw = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
    login_psw.send_keys(user["password"])

    signin_btn = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')))
    signin_btn.click()
    time.sleep(5)