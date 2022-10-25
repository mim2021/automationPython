import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Pages.loginpage import Login
from Pages.logoutpage import Logout

# unittest
class test_login_logout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.get("https://sharetrip.net/")
        cls.driver.maximize_window()

    def test1_login(self):
        driver = self.driver
        driver.implicitly_wait(10)

        login = Login(driver)
        login.click_profile_icon()
        login.click_login()
        login.enter_email("mim@sharetrip.net")
        login.enter_password("vugijugi")
        login.click_login_button()

        logout = Login(driver)
        logout.click_profile_icon()

        logout = Logout(driver)
        logout.click_logout()

        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

# if __name__ == '__main__':
#     unittest.main()
# print("Successfully Run")
