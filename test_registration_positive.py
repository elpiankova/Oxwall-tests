import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration_success(driver):
    username = 'iryna123'
    email = "automation@oxwall.com"
    password = "pass1"
    name = "first and last NAME"

    user_reg = driver.find_element_by_class_name("ow_console_item_link")
    user_reg.click()

    time.sleep(3)

    reg_form_header = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ow_ic_user"))
    )
    #
    # # el = driver.find_element_by_class_name("ow_ic_user")
    # #
    # # print(el)
    #
    assert "Register" in reg_form_header.text

    username1 = WebDriverWait(driver, 5).until(
        EC.visibility_of_any_elements_located((By.CLASS_NAME, "ow_username_validator"))
    )[0]

    username1.click()
    username1.send_keys(username)

    email1 = driver.find_element_by_class_name("ow_email_validator")
    email1.click()
    email1.send_keys(email)

    password1 = WebDriverWait(driver, 5).until(
        EC.visibility_of_any_elements_located((By.NAME, "password"))
    )[0]
    password1.click()
    password1.send_keys(password)

    password2 = WebDriverWait(driver, 5).until(
        EC.visibility_of_any_elements_located((By.NAME, "repeatPassword"))
    )[0]

    password2.click()
    password2.send_keys(password)

    real_name = WebDriverWait(driver, 5).until(
        EC.visibility_of_any_elements_located((By.XPATH, ("//*[contains(text(),'Real name')]")))
    )[0]
    real_name.click()
    real_name = driver.switch_to_active_element()
    real_name.send_keys(Keys.SPACE)
    real_name.send_keys(name)

# select gender
    gender_female = WebDriverWait(driver, 5).until(
        EC.visibility_of_any_elements_located((By.XPATH, ("//*[contains(text(),'Female')]")))
    )[0]
    gender_female.click()

# select Birthday
    # select day
    day = WebDriverWait(driver, 5).until(
        EC.visibility_of_any_elements_located((By.XPATH, ("//*[contains(@name,'day')]")))
    )[0]
    day.click()
    day.find_element_by_xpath('./option[6]').click()
    # select month
    month = WebDriverWait(driver, 5).until(
        EC.visibility_of_any_elements_located((By.XPATH, ("//*[contains(@name,'month')]")))
    )[0]
    month.click()
    month.find_element_by_xpath('./option[6]').click()
    # select year
    year = WebDriverWait(driver, 5).until(
        EC.visibility_of_any_elements_located((By.XPATH, ("//*[contains(@name,'year')]")))
    )[0]
    year.click()
    year.find_element_by_xpath('./option[6]').click()

# select looking for option
    looking_for = WebDriverWait(driver, 5).until(
        EC.visibility_of_any_elements_located((By.XPATH, ("//*[contains(text(),'Male')]")))
    )[1]
    looking_for.click()

# select Here for option
    friendship = WebDriverWait(driver, 5).until(
        EC.visibility_of_any_elements_located((By.XPATH, ("//*[contains(text(),'Friendship')]")))
    )[0]
    friendship.click()

# fill in interests
    music_interests = WebDriverWait(driver, 5).until(
        EC.visibility_of_any_elements_located((By.XPATH, ("//*[contains(text(),'Music')]")))
    )[0]
    music_interests.click()
    music_interests = driver.switch_to_active_element()
    music_interests.send_keys(Keys.SPACE)
    music_interests.send_keys('rock jazz whatever 123 !@#')
    time.sleep(7)

