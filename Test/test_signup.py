import string
import time
import unittest
import random
from Pages.signuppage import SignUp
import pytest


@pytest.mark.usefixtures("test_setup")
class TestSignUp(unittest.TestCase):
    # @pytest.mark.run('first')
    def test1_valid_signup(self):
        driver = self.driver
        signup = SignUp(driver)
        signup.click_profile_icon_signup()
        signup.click_create_account_text()

        # signup.enter_email_signup(''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@gmail.com")
        # input_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        def get_random_string(length=1):
            letters = string.ascii_letters
            random_string = ''.join(random.choice(letters) for _ in range(length))
            return random_string
        email = f"{get_random_string(10)}@gmail.com"
        input_password = f"{get_random_string(15)}{random.randrange(100000)}"
        print(email)
        print(input_password)

        signup.enter_email_signup(email)
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
        signup.enter_email_signup(''.join(random.choices(string.ascii_lowercase + string.digits, k=15)) + "@gmail.com")
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
        input_password = random.choices(string.ascii_uppercase, k=10)
        signup.enter_password_signup(input_password)
        driver.execute_script("window.scrollTo(0, 200)")
        signup.enter_confirm_password_signup(input_password)
        signup.click_signup_button()
        time.sleep(4)
