import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MultiCityFlight:
    def __init__(self, driver):
        self.driver = driver
        self.multiCityTab = "//body/div[@id='__next']/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[3]"
        self.flyingFromMultiCity1 = "//input[@id='autocomplete0origin']"
        self.flyingToMultiCity1 = "//input[@id='autocomplete0destination']"
        self.flyingFromMultiCity2 = "//input[@id='autocomplete1origin']"
        self.flyingToMultiCity2 = "//input[@id='autocomplete1destination']"
        self.flyingFromMultiCity3 = "//input[@id='autocomplete2origin']"
        self.flyingToMultiCity3 = "//input[@id='autocomplete2destination']"
        self.searchButton = "//body/div[@id='__next']/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[2]/button[1]"

    def click_multi_city_tab(self):
        self.driver.find_element(By.XPATH, self.multiCityTab).click()

    def input_multi_city_flying_from1(self, flying_from_country1):
        self.driver.find_element(By.XPATH, self.flyingFromMultiCity1).click()
        self.driver.find_element(By.XPATH, self.flyingFromMultiCity1).send_keys(flying_from_country1)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()

    def input_multi_city_flying_to1(self, flying_to_country1):
        self.driver.find_element(By.XPATH, self.flyingToMultiCity1).click()
        self.driver.find_element(By.XPATH, self.flyingToMultiCity1).send_keys(flying_to_country1)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()

    def input_city_flying_from2(self, flying_from_country2):
        self.driver.find_element(By.XPATH, self.flyingFromMultiCity2).click()
        self.driver.find_element(By.XPATH, self.flyingFromMultiCity2).send_keys(flying_from_country2)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        action.send_keys(Keys.ENTER).perform()

    def input_city_flying_to2(self, flying_to_country2):
        self.driver.find_element(By.XPATH, self.flyingFromMultiCity3).click()
        self.driver.find_element(By.XPATH, self.flyingToMultiCity3).send_keys(flying_to_country2)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        action.send_keys(Keys.ENTER).perform()

    def input_city_flying_from3(self, flying_from_country3):
        self.driver.find_element(By.XPATH, self.flyingToMultiCity3).click()
        self.driver.find_element(By.XPATH, self.flyingToMultiCity3).send_keys(flying_from_country3)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        action.send_keys(Keys.ENTER).perform()


