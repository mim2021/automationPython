import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# class Config:
@pytest.fixture(scope="class", autouse=True)
def test_setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = driver
    driver.maximize_window()
    driver.get("https://sharetrip.net/")
    driver.implicitly_wait(10)
    yield
    driver.close()
    print("Successfully tested")
