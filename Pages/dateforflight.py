from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DateForFlights:
    def __init__(self, driver):
        self.driver = driver

    multiTab = (By.XPATH, "(//div[@role='tablist'])[2]")
    dateInput = (By.ID, "date_input")
    rightArrowSignOneWay = (By.XPATH, "(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeLarge mdi mdi-chevron-right mui-style-1w8s6so'])[1]")

    def select_target_date(self, month_year, date):
        is_month_found = False
        self.get_element(self.dateInput).click()

        while not is_month_found:
            month_year_locator = (By.XPATH, f'//div[contains(@class, "CalendarMonth_caption")]//strong[text()="{month_year}"]')

            if self.is_element_visible(month_year_locator, 3):
                is_month_found = True
                date_locator = (By.XPATH, f'//strong[text()="{month_year}"]/parent::div//following-sibling::table//td')

                for index in range(len(self.get_elements(date_locator))):
                    target_date_element = self.get_elements(date_locator)[index]
                    target_date_text = int(target_date_element.text.strip())
                    if target_date_text == date:
                        self.scroll_to_element(self.multiTab)
                        target_date_element.click()
                        break
            else:
                self.get_element(self.rightArrowSignOneWay).click()
        print('Selected date:', self.get_element(self.dateInput).get_attribute("value"))

    def get_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def get_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def is_element_visible(self, locator, wait_time=10):
        try:
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def select_return_date(self, month_year, date):
        is_month_found = False
        self.get_element(self.dateInput).click()

        while not is_month_found:
            month_year_locator = (By.XPATH, f'//div[contains(@class, "CalendarMonth_caption")]//strong[text()="{month_year}"]')

            if self.is_element_visible(month_year_locator, 3):
                is_month_found = True
                date_locator = (By.XPATH, f'//strong[text()="{month_year}"]/parent::div//following-sibling::table//td')

                for index in range(len(self.get_elements(date_locator))):
                    target_date_element = self.get_elements(date_locator)[index]
                    target_date_text = int(target_date_element.text.strip())
                    if target_date_text == date:
                        self.scroll_to_element(self.multiTab)
                        target_date_element.click()
                        break
            else:
                self.get_element(self.rightArrowSignOneWay).click()
        print('Selected date:', self.get_element(self.dateInput).get_attribute("value"))


    def scroll_to_element(self, locator):
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)



