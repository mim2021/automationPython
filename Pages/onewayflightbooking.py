import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class OneWayFlight:
    def __init__(self, driver):
        self.driver = driver
        self.oneway_tab = "//span[contains(text(),'One Way')]"
        self.flying_from_oneway = "//body/div[@id='__next']/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]"
        self.bkk_oneway = "//small[contains(text(),'Thailand, Suvarnabhumi Airport (BKK)')]"
        self.flying_to_oneway = "//div[@class='icon-input-block search-group circle-left']//div[@class='text-field']//div//input[@id='autocompleteundefined']"
        self.kua_oneway = "//small[contains(text(),'Malaysia, Kuantan Airport (KUA)')]"
        self.select_date = "date_input"
        self.right_arrow_sign = "//button[@class='MuiButtonBase-root MuiIconButton-root mdi mdi-chevron-right']"
        self.choose_date = "//span[contains(text(),'28')]"

    def click_oneway_tab(self):
        self.driver.find_element(By.XPATH, self.oneway_tab).click()

    def input_flying_from_oneway(self, country_flying_from):
        self.driver.find_element(By.XPATH, self.flying_from_oneway).click()
        self.driver.find_element(By.XPATH, self.flying_from_oneway).send_keys(country_flying_from)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()

    def input_flying_to_oneway(self, country_flying_to):
        self.driver.find_element(By.XPATH, self.flying_to_oneway).click()
        self.driver.find_element(By.XPATH, self.flying_to_oneway).send_keys(country_flying_to)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()

    def click_select_date_oneway(self):
        self.driver.find_element(By.ID, self.select_date).click()
        time.sleep(1)

    def click_arrow(self):
        self.driver.find_element(By.XPATH, self.right_arrow_sign).click()
        time.sleep(1)

    def click_date(self):
        self.driver.find_element(By.XPATH, self.choose_date).click()
        time.sleep(1)






