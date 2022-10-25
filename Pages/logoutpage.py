import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("test_setup")
class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.logout_text = "//li[normalize-space()='Log Out']"

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_text).click()

