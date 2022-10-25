import string
import time
import unittest
import pytest
from Pages.loginpage import Login
from Pages.logoutpage import Logout
import random

@pytest.mark.usefixtures("test_setup")
class TestLoginLogout(unittest.TestCase):
    @pytest.mark.one1
    def test_valid_login(self):
        driver = self.driver
        login = Login(driver)
        login.click_profile_icon()
        login.click_login()
        login.enter_email("mim@sharetrip.net")
        login.enter_password("vugijugi")
        login.click_login_button()

        logout = Login(driver)
        logout.click_profile_icon()

        logout = Logout(driver)
        time.sleep(4)
        logout.click_logout()
        actual_title = driver.title
        expected_title = "ShareTrip™️:Best Travel Agency in Bangladesh - Flights & Hotels"
        message = "title is same"
        self.assertEqual(actual_title, expected_title, message)
        time.sleep(4)

    @pytest.mark.two2
    def test_invalid_login(self):
        driver = self.driver
        login = Login(driver)
        login.click_profile_icon()
        login.click_login()
        login.enter_email(string.ascii_lowercase + "@gmail.com")
        login.enter_password(string.ascii_letters+string.digits+string.punctuation)
        login.click_login_button()

        logout = Login(driver)
        logout.click_profile_icon()

        logout = Logout(driver)
        time.sleep(4)
        logout.click_logout()

        time.sleep(4)
