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

def test_add_feed_success_text(driver, logged_user, log_out):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "status"))
        )
    except:
        pass
    status_elements = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")
    new_status_field = driver.find_element_by_name("status")
    new_status_field.click()
    input_text = "Text for testing newsfeed"
    new_status_field.send_keys(input_text)
    driver.find_element_by_name("save").click()
    time.sleep(5)

    # check if new feed added
    status_elements = WebDriverWait(driver, 10).until(presence_of_N_elements_located(
            (By.CLASS_NAME, "ow_newsfeed_item"),
            len(status_elements)+1),
        message="Can't find correct count of elements"
    )


def test_add_feed_success_picture(driver, logged_user, log_out):
    new_status_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "status"))
        )
    status_elements = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")
    new_status_field.click()
    add_file = driver.find_element_by_xpath('//a[contains(@id, "nfa-feed")]/input')
    add_file.send_keys(r'C:\Users\Admin\PycharmProjects\Selenium\test_cloud.jpg')
    preload_photo = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@class = 'ow_photo_attachment_pic ow_attachment_preload']"))
    )

    driver.find_element_by_name("save").click()

    status_elements = WebDriverWait(driver, 10).until(presence_of_N_elements_located(
            (By.CLASS_NAME, "ow_newsfeed_item"),
            len(status_elements)+1),
        message="Can't find correct count of elements"
    )

    newsfeed = driver.find_element_by_css_selector(".ow_newsfeed_string.ow_small.ow_smallmargin")
    assert ("uploaded 1 new photo" in newsfeed.text) and ("Newsfeed Photos" in newsfeed.text)



