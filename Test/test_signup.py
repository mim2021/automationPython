import string
import time
import unittest
import random

from selenium.webdriver import ActionChains, Keys

from Pages.signuppage import SignUp

import pytest


@pytest.mark.usefixtures("test_setup")
class TestSignUp(unittest.TestCase):
    # @pytest.mark.run('first')
    def test1_valid_signup(self):
        driver = self.driver
        driver.get("https://sharetrip.net/")
        signup = SignUp(driver)
        signup.click_profile_icon_signup()
        signup.click_create_account_text()
        signup.enter_email_signup(''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@gmail.com")
        time.sleep(3)
        input_password = random.choices(string.ascii_letters + string.digits, k=10)
        signup.enter_password_signup(input_password)
        driver.execute_script("window.scrollTo(0, 200)")
        signup.enter_confirm_password_signup(input_password)
        signup.click_signup_button()
        time.sleep(4)

    """negative test case for failed sign up"""

    # password length is less than eight

    def test2_invalid_signup(self):
        driver = self.driver
        driver.get("https://sharetrip.net/")
        signup = SignUp(driver)
        signup.click_profile_icon_signup()
        signup.click_create_account_text()
        signup.enter_email_signup(''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@gmail.com")
        time.sleep(3)
        input_password = random.choices(string.ascii_letters + string.digits, k=7)
        signup.enter_password_signup(input_password)
        driver.execute_script("window.scrollTo(0, 200)")
        signup.enter_confirm_password_signup(input_password)
        signup.click_signup_button()
        time.sleep(4)

    """password is without number"""

    def test3_invalid_signup(self):
        driver = self.driver
        driver.get("https://sharetrip.net/")
        signup = SignUp(driver)
        signup.click_profile_icon_signup()
        signup.click_create_account_text()
        signup.enter_email_signup(''.join(random.choices(string.ascii_lowercase, k=8)) + "@gmail.com")
        time.sleep(3)
        input_password = random.choices(string.ascii_letters, k=9)
        signup.enter_password_signup(input_password)
        driver.execute_script("window.scrollTo(0, 200)")
        signup.enter_confirm_password_signup(input_password)
        signup.click_signup_button()
        time.sleep(4)

    """password is without uppercase"""

    def test4_invalid_signup(self):
        driver = self.driver
        driver.get("https://sharetrip.net/")
        signup = SignUp(driver)
        signup.click_profile_icon_signup()
        signup.click_create_account_text()
        signup.enter_email_signup(''.join(random.choices(string.ascii_lowercase, k=10)) + "@gmail.com")
        time.sleep(3)
        input_password = random.choices(string.ascii_lowercase, k=10)
        signup.enter_password_signup(input_password)
        driver.execute_script("window.scrollTo(0, 200)")
        signup.enter_confirm_password_signup(input_password)
        signup.click_signup_button()
        time.sleep(4)

    """password is without lowercase"""

    def test5_invalid_signup(self):
        driver = self.driver
        driver.get("https://sharetrip.net/")
        signup = SignUp(driver)
        signup.click_profile_icon_signup()
        signup.click_create_account_text()
        signup.enter_email_signup(''.join(random.choices(string.ascii_lowercase, k=10)) + "@gmail.com")
        time.sleep(2)
        input_password = random.choices(string.ascii_uppercase, k=10)
        signup.enter_password_signup(input_password)
        driver.execute_script("window.scrollTo(0, 200)")
        signup.enter_confirm_password_signup(input_password)
        signup.click_signup_button()
        time.sleep(4)
