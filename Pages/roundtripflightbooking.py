import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class RoundTripFlight:
    def __init__(self, driver):
        self.driver = driver
        self.flyingFromRoundTrip = "//body/div[@id='__next']/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]"
        self.flyingToRoundTrip = "//body/div[@id='__next']/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/input[1]"

    def input_flying_from_roundtrip(self, country_flying_from):
        self.driver.find_element(By.XPATH, self.flyingFromRoundTrip).click()
        self.driver.find_element(By.XPATH, self.flyingFromRoundTrip).send_keys(country_flying_from)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()

    def input_flying_to_roundtrip(self, country_flying_to):
        self.driver.find_element(By.XPATH, self.flyingToRoundTrip).click()
        self.driver.find_element(By.XPATH, self.flyingToRoundTrip).send_keys(country_flying_to)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()
