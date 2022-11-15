import time

from selenium.webdriver.common.by import By
from Pages.onewayflightbooking import OneWayFlight


class DateForFlights:
    def __init__(self, driver):
        self.driver = driver
        self.selectDate = "date_input"
        self.rightArrowSignOneWay = "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeLarge mdi mdi-chevron-right css-1w8s6so']"

    def select_target_date(self, month_year, date):
        self.driver.find_element(By.ID, self.selectDate).click()
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.ID, self.selectDate))
        is_month_found = False

        while not is_month_found:
            month_year_locator = (By.XPATH, f'//div[contains(@class, "CalendarMonth_caption")]//strong[text()="{month_year}"]')
            if len(self.driver.find_elements(*month_year_locator)) == 1:
                is_month_found = True
                # date_td_locator = (By.XPATH, f'//strong[text()="{month_year}"]/parent::div//following-sibling::table//td')
                date_text_locator = (By.XPATH, f'//strong[text()="{month_year}"]/parent::div//following-sibling::table//td//span[@class="d"]')
                print('len', len(self.driver.find_elements(*date_text_locator)))

                for date_element in self.driver.find_elements(*date_text_locator):
                    text = date_element.text
                    print('.....................', text)
                    if text == date:
                        date_element.click()
                        print('Selected date:', self.driver.find_element(By.XPATH, self.rightArrowSignOneWay).get_attribute("value"))
            else:
                self.driver.find_element(By.XPATH, self.rightArrowSignOneWay).click()


