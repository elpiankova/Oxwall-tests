from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from custom_wait_conditions import presence_of_N_elements_located
import time
import os
import re
import pytest

@pytest.fixture(scope="session")
def base_url():
    base_url = "http://127.0.0.1/oxwall/"
    return base_url


@pytest.fixture(scope="session")
def driver(base_url):
    dr = webdriver.Chrome()
    dr.get(base_url)
    yield dr
    dr.quit()


@pytest.fixture()
def username():
    return "admin"


@pytest.fixture()
def logged_user(driver, username):
    password = "pass"
    user_login = driver.find_element_by_class_name("ow_signin_label")
    user_login.click()
    # login
    elem1 = driver.find_element_by_name("identity")
    elem1.send_keys(Keys.CONTROL + "a")
    elem1.send_keys(Keys.DELETE)
    elem1.send_keys(username)
    elem2 = driver.find_element_by_name("password")
    elem2.send_keys(Keys.CONTROL + "a")
    elem2.send_keys(Keys.DELETE)
    elem2.send_keys(password)
    driver.find_element_by_name("submit").click()

@pytest.fixture()
def log_out(base_url, driver, username):
    yield
    menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f'div.ow_console_right a[href="{base_url}user/{username}"]')),
        message="Can't find User menu"
    )

    sign_out = driver.find_element_by_css_selector(f'div.ow_console_right [href="{base_url}sign-out"]')
    action = ActionChains(driver)
    action.move_to_element(menu)
    action.click(sign_out)
    action.perform()
