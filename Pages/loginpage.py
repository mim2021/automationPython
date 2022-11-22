import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("test_setup")
class Login:
    def __init__(self, driver):
        self.driver = driver
        self.profile_icon = "//div[@class='image flex-img d-flex align-items-center justify-content-center']"
        self.login_text = "//body/div[@id='account-menu']/div[3]/ul[1]/li[1]"
        self.email_box_login = "email"
        self.password_box_login = "password"
        self.eye_icon_login = "//button[@class='MuiButtonBase-root MuiIconButton-root']"
        self.login_button_xpath = "//button[@type='submit']"

    def click_profile_icon_login(self):
        self.driver.find_element(By.XPATH, self.profile_icon).click()

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_text).click()

    def enter_email_login(self, email):
        login_email = self.driver.find_element(By.ID, self.email_box_login)
        login_email.click()
        login_email.send_keys(email)

    def enter_password_login(self, password):
        login_password = self.driver.find_element(By.ID, self.password_box_login)
        login_password.click()
        login_password.send_keys(password)

    def click_eye_icon_login(self):
        self.driver.find_element(By.XPATH, self.eye_icon_login).click()

    def click_login_button(self):
        login_button = self.driver.find_element(By.XPATH, self.login_button_xpath)
        login_button.click()
        # self.driver.execute_script("arguments[0].click();", login_button)


