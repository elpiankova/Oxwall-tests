import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from oxwall_helper import OxwallHelper

def test_login_success(driver, username, log_out):
    app = OxwallHelper(driver)
    password = "pass"
    app.login_as(username, password)
    message_popup = app.message()

    assert "SUCCESS" in message_popup.text

    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "status"))
    )

    assert driver.find_element_by_xpath('//h1[text()="My Dashboard"]')

def test_login_error(driver, username):
    app = OxwallHelper(driver)
    password = "fail"
    #login
    app.login_as(username, password)
    # message
    message_popup = app.message()

    assert "INVALID" in message_popup.text










