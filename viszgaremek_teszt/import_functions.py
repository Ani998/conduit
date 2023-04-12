from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

def registration(browser):
    sign_up_btn = browser.find_element(By.LINK_TEXT, 'Sign up')
    sign_up_btn.click()

    reg_username = browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
    reg_username.send_keys("Valami")
    reg_email = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
    reg_email.send_keys("valami28@gmail.com")
    reg_psw = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
    reg_psw.send_keys("Strukturavaltas3")

    reg_btn = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    reg_btn.click()

    time.sleep(5)
    ok_btn = browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
    ok_btn.click()
    time.sleep(3)
def login(browser):
    login_btn = browser.find_element(By.XPATH, '//a[@href="#/login"]')
    login_btn.click()

    login_email = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
    login_email.send_keys("Valami24@gmail.com")
    login_psw = browser.find_element(By.XPATH, '//input[@placeholder = "Password"]')
    login_psw.send_keys("Strukturavaltas3")

    login_btn_send = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    login_btn_send.click()

    time.sleep(5)