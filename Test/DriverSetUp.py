import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.set_page_load_timeout(10)
driver.get("https://sharetrip.net/")
driver.maximize_window()
driver.find_element(By.XPATH, "//div[@class='image flex-img d-flex align-items-center justify-content-center']").click()
time.sleep(4)

driver.close()
