import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("test_setup")
class SignUp:
    def __init__(self, driver):
        self.driver = driver
        self.profile_icon = "//div[@class='image flex-img d-flex align-items-center justify-content-center']"
        self.create_account = "//li[contains(text(),'Create An Account')]"
        self.email_box_signup = "email"
        self.password_box_signup = "password"
        self.password_eye_icon = "//body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]"
        self.password_confirmation_box_signup = "password_confirmation"
        self.confirm_password_eye_icon = "//body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/button[1]"
        self.signup_button = "//span[normalize-space()='Sign Up']"

    def click_profile_icon_signup(self):
        self.driver.find_element(By.XPATH, self.profile_icon).click()

    def click_create_account_text(self):
        self.driver.find_element(By.XPATH, self.create_account).click()

    def enter_email_signup(self, username):
        self.driver.find_element(By.ID, self.email_box_signup).click()
        self.driver.find_element(By.ID, self.email_box_signup).send_keys(username)

    def enter_password_signup(self, password):
        self.driver.find_element(By.ID, self.password_box_signup).click()
        self.driver.find_element(By.ID, self.password_box_signup).send_keys(password)
        self.driver.find_element(By.XPATH, self.password_eye_icon).click()

    def enter_confirm_password_signup(self, confirm_password):
        self.driver.find_element(By.ID, self.password_confirmation_box_signup).click()
        self.driver.find_element(By.ID, self.password_confirmation_box_signup).send_keys(confirm_password)
        self.driver.find_element(By.XPATH, self.confirm_password_eye_icon).click()

    def click_signup_button(self):
        self.driver.find_element(By.XPATH, self.signup_button).click()




