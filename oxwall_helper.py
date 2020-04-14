from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from custom_wait_conditions import presence_of_N_elements_located

class OxwallHelper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.action = ActionChains(self.driver)

    def message(self):
        message_popup = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "ow_message_node"))
        )
        return message_popup

    def login_as(self, username, password):
        driver = self.driver
        user_login = driver.find_element_by_class_name("ow_signin_label")
        user_login.click()
        elem1 = driver.find_element_by_name("identity")
        elem1.send_keys(Keys.CONTROL + "a")
        elem1.send_keys(Keys.DELETE)
        elem1.send_keys(username)
        elem2 = driver.find_element_by_name("password")
        elem2.send_keys(Keys.CONTROL + "a")
        elem2.send_keys(Keys.DELETE)
        elem2.send_keys(password)
        driver.find_element_by_name("submit").click()

    def get_statuses(self):
        status_elements = self.driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")
        return status_elements

    def wait_statues_to_show(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "status"))
        )

    def create_new_status(self, input_text):
        new_status_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "status"))
        )
        new_status_field.click()
        new_status_field.send_keys(input_text)
        self.driver.find_element_by_name("save").click()

    def check_new_status_added(self, status_elements):
        status_elements = WebDriverWait(self.driver, 10).until(presence_of_N_elements_located(
            (By.CLASS_NAME, "ow_newsfeed_item"),
            len(status_elements) + 1),
            message="Can't find correct count of elements"
        )

    def add_new_status_file(self, input_file):
        new_status_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "status"))
        )
        new_status_field.click()
        add_file = self.driver.find_element_by_xpath('//a[contains(@id, "nfa-feed")]/input')
        add_file.send_keys(input_file)
        preload_photo = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@class = 'ow_photo_attachment_pic ow_attachment_preload']"))
        )
        self.driver.find_element_by_name("save").click()

    def find_by_xpath_and_click(self, elm_xpath):
        element = self.wait.until(
            EC.visibility_of_any_elements_located((By.XPATH, elm_xpath))
        )[0]
        element.click()
        return element

    def find_by_name_and_click(self, elm_name):
        element = self.wait.until(
                EC.visibility_of_any_elements_located((By.NAME, elm_name))
            )[0]
        element.click()
        return element


