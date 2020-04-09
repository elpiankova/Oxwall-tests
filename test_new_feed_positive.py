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
from oxwall_helper import OxwallHelper

def test_add_feed_success_text(driver, logged_user, log_out):
    app = OxwallHelper(driver)
    # get statuses
    status_elements = app.get_statuses()

    # wait for statuses to show
    app.wait_statues_to_show()
    input_text = "Text for testing newsfeed"
    app.create_new_status(input_text)

    app.wait_statues_to_show()

    # check if new feed added
    app.check_new_status_added(status_elements)

def test_add_feed_success_picture(driver, logged_user, log_out):
    app = OxwallHelper(driver)
    # get statuses
    status_elements = app.get_statuses()
    # wait for statuses to show
    app.wait_statues_to_show()
    # add new file
    app.add_new_status_file(input_file=r'C:\Users\Admin\PycharmProjects\Selenium\test_cloud.jpg')
    # check new status was added
    app.check_new_status_added(status_elements)
    # check page objects loaded
    newsfeed = driver.find_element_by_css_selector(".ow_newsfeed_string.ow_small.ow_smallmargin")
    assert ("uploaded 1 new photo" in newsfeed.text) and ("Newsfeed Photos" in newsfeed.text)






