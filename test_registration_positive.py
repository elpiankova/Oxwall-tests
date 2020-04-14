import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from oxwall_helper import OxwallHelper

def test_registration_success(driver):
    app = OxwallHelper(driver)
    username = 'iryna123'
    email = "automation@oxwall.com"
    password = "pass1"
    name = "first and last NAME"

    user_reg = driver.find_element_by_class_name("ow_console_item_link")
    user_reg.click()

    reg_form_header = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ow_ic_user"))
    )

    assert "Register" in reg_form_header.text

    username1 = WebDriverWait(driver, 5).until(
        EC.visibility_of_any_elements_located((By.CLASS_NAME, "ow_username_validator"))
    )[0]
    username1.click()
    username1.send_keys(username)

    email1 = driver.find_element_by_class_name("ow_email_validator")
    email1.click()
    email1.send_keys(email)

    password1 = app.find_by_name_and_click("password")
    password1.send_keys(password)

    password2 = app.find_by_name_and_click("repeatPassword")
    password2.send_keys(password)

    real_name = app.find_by_xpath_and_click(("//*[contains(text(),'Real name')]"))
    real_name = driver.switch_to_active_element()
    real_name.send_keys(Keys.SPACE)
    real_name.send_keys(name)

# select gender
    app.find_by_xpath_and_click(("//*[contains(text(),'Female')]"))

    # select Birthday - day

    day = app.find_by_xpath_and_click(("//*[contains(@name,'day')]"))
    day.find_element_by_xpath('./option[6]').click()
    # select Birthday - month
    month = app.find_by_xpath_and_click(("//*[contains(@name,'month')]"))
    month.find_element_by_xpath('./option[6]').click()
    # select Birthday - year
    year = app.find_by_xpath_and_click(("//*[contains(@name,'year')]"))
    year.find_element_by_xpath('./option[6]').click()

# select looking for option
    looking_for = app.find_by_xpath_and_click(("//*[contains(text(),'Male')]"))

# select Here for option
    friendship = app.find_by_xpath_and_click(("//*[contains(text(),'Friendship')]"))

# fill in interests
    music_interests = app.find_by_xpath_and_click(("//*[contains(text(),'Music')]"))
    music_interests = driver.switch_to_active_element()
    music_interests.send_keys(Keys.SPACE)
    music_interests.send_keys('rock jazz whatever 123 !@#')
    time.sleep(7)

    join_btn = driver.find_element_by_class_name('ow_button.ow_ic_submit')
    join_btn.click()
    message_popup = app.message()
    assert "SUCCESS" in message_popup.text
    app.wait_statues_to_show()
    assert driver.find_element_by_xpath('//h1[text()="My Dashboard"]')






