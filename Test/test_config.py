import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Config:
    @pytest.fixture(scope = "session", autouse=True)
    def test_setup(self):
        driver = self.driver
        self.driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
        self.driver.set_page_load_timeout(10)
        self.driver.get("https://sharetrip.net/")
        self.driver.maximize_window()
        yield
        self.driver.close()
