import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver, username, log_out):
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
    message_popup = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ow_message_node"))
    )

    assert "SUCCESS" in message_popup.text

    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "status"))
    )

    assert driver.find_element_by_xpath('//h1[text()="My Dashboard"]')

def test_login_error(driver, username, log_out):
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

# message_popup = driver.find_element_by_class_name("ow_message_node")
# assert ("uploaded 1 new photo" in newsfeed.text) and ("Newsfeed Photos" in newsfeed.text)







