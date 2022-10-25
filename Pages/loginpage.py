import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("test_setup")
class Login:
    def __init__(self, driver):
        self.driver = driver
        self.profile_icon = "//div[@class='image flex-img d-flex align-items-center justify-content-center']"
        self.login_text = "//li[normalize-space()='Log In']"
        self.email_box = "email"
        self.password_box = "password"
        self.login_button_xpath = "//button[@type='submit']"

    def click_profile_icon(self):
        self.driver.find_element(By.XPATH, self.profile_icon).click()

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_text).click()

    def enter_email(self, email):
        login_email = self.driver.find_element(By.ID, self.email_box)
        login_email.click()
        login_email.send_keys(email)

    def enter_password(self, password):
        login_password = self.driver.find_element(By.ID, self.password_box)
        login_password.click()
        login_password.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.XPATH, self.login_button_xpath)
        login_button.click()
