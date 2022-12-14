import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class HotelBooking:
    def __init__(self, driver):
        self.driver = driver
        self.hotelTab = "//body/div[@id='__next']/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/span[1]"
        self.enterCity = "//input[@id='hotelAutocomplete']"
        self.checkInDate = "//input[@id='startDateId']"
        self.checkOutDate = "//input[@id='endDateId']"

    def click_hotel_tab(self):
        ele1 = self.driver.find_element(By.XPATH, self.hotelTab)
        self.driver.execute_script("arguments[0].click();", ele1)

    def enter_city_input(self, city_name):
        self.driver.find_element(By.XPATH, self.enterCity).click()
        self.driver.find_element(By.XPATH, self.enterCity).send_keys(city_name)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()
















