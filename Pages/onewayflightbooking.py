import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OneWayFlight:
    def __init__(self, driver):
        self.driver = driver
        self.onewayTab = "//span[contains(text(),'One Way')]"
        self.flyingFromOneWay = "//body/div[@id='__next']/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]"
        # self.bkkOneway = "//small[contains(text(),'Thailand, Suvarnabhumi Airport (BKK)')]"
        self.flyingToOneWay = "//div[@class='icon-input-block search-group circle-left']//div[@class='text-field']//div//input[@id='autocompleteundefined']"
        # self.kua_oneway = "//small[contains(text(),'Malaysia, Kuantan Airport (KUA)')]"
        self.selectDate = "date_input"
        self.rightArrowSignOneWay = "//button[@class='MuiButtonBase-root MuiIconButton-root mdi mdi-chevron-right']"
        self.chooseDateOneWay = "//td[@aria-label='Thursday, January 19, 2023']//span[@class='d'][normalize-space()='19']"
        self.economyClass = "//span[contains(text(),'Economy Class')]"
        self.searchButton = "//span[normalize-space()='Search Flights']"
        self.bookButton = "//div[@name='scroll-to-element']//div[2]//div[1]//div[2]//div[3]//a[1]//span[1]"
        self.title = "//*[@id='mui-component-select-titleName']"
        self.msTitle = "//li[normalize-space()='Ms']"
        self.givenNameField = "givenName"
        self.surNameField = "//input[@name='surName']"
        self.radio_button = "//span[normalize-space()='I want to Earn Trip Coin']"
        self.phoneNumberField = "//input[@name='mobileNumber']"
        self.DOB = "//*[@id='__next']/div/section/div/div/div[1]/div[2]/div/div/form/section/div[1]/div[4]/div[3]/div/div/div/div[1]/div/div/div/input"
        self.monthDOB = "//select[@class='react-datepicker__month-select']"
        self.yearDOB = "//select[@class='react-datepicker__year-select']"
        self.dayDOB = "//div[@aria-label='Choose Friday, January 18th, 1980']"
        self.postCode = "//input[@name='postCode']"
        self.passportNumber = "//input[@name='passportNumber']"
        self.bank = "//label[@for='inlineRadio1']"
        self.quickPickCheckBox = "//input[@name='quickPick']"
        self.tcCheckBox = "//input[@name='checkedB']"
        self.paynowButton = "//span[normalize-space()='Pay now']"
        self.passportExpiryDateField = "//*[@id='__next']/div/section/div/div/div[1]/div[2]/div/div/form/section/div[1]/div[4]/div[7]/div/div/div/div[1]/div/div/div/input"
        self.passportExpiryMonth = "//select[@class='react-datepicker__month-select']"
        self.passportExpiryYear = "//select[@class='react-datepicker__year-select']"
        self.passportExpiryDate = "//div[@aria-label='Choose Wednesday, June 19th, 2024']"

    def click_oneway_tab(self):
        self.driver.find_element(By.XPATH, self.onewayTab).click()

    def input_flying_from_oneway(self, country_flying_from):
        self.driver.find_element(By.XPATH, self.flyingFromOneWay).click()
        self.driver.find_element(By.XPATH, self.flyingFromOneWay).send_keys(country_flying_from)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()

    def input_flying_to_oneway(self, country_flying_to):
        self.driver.find_element(By.XPATH, self.flyingToOneWay).click()
        self.driver.find_element(By.XPATH, self.flyingToOneWay).send_keys(country_flying_to)
        driver = self.driver
        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()

    def click_select_date_oneway(self):
        self.driver.find_element(By.ID, self.selectDate).click()

    def click_arrow(self):
        self.driver.find_element(By.XPATH, self.rightArrowSignOneWay).click()

    def click_date(self):
        self.driver.find_element(By.XPATH, self.chooseDateOneWay).click()

    def click_economy(self):
        self.driver.find_element(By.XPATH, self.economyClass).click()

    def click_search_button(self):
        driver = self.driver
        self.driver.find_element(By.XPATH, self.searchButton)
        act = ActionChains(driver)
        act.double_click().perform()
        self.driver.find_element(By.XPATH, self.searchButton).click()

    def click_book_button(self):
        self.driver.find_element(By.XPATH, self.bookButton).click()

    def switch_window(self):
        driver = self.driver
        print(driver.current_window_handle)
        driver.switch_to.window(driver.window_handles[1])
        print(driver.window_handles)

    def click_title(self):
        self.driver.find_element(By.XPATH, self.title).click()
        self.driver.find_element(By.XPATH, self.msTitle).click()

    def input_given_name(self, given_name):
        self.driver.find_element(By.NAME, self.givenNameField).click()
        self.driver.find_element(By.NAME, self.givenNameField).send_keys(given_name)

    def input_sur_name(self, sur_name):
        # self.driver.find_element(By.XPATH, self.surNameField).clear()
        self.driver.find_element(By.XPATH, self.surNameField).send_keys(sur_name)

    def click_radio_button(self):
        self.driver.find_element(By.XPATH, self.radio_button).click()

    def input_phone_number(self, mobile_number):
        self.driver.find_element(By.XPATH, self.phoneNumberField).click()
        # self.driver.find_element(By.XPATH, self.phoneNumberField).clear()
        self.driver.find_element(By.XPATH, self.phoneNumberField).send_keys(mobile_number)

    def select_DOB(self):
        self.driver.find_element(By.XPATH, self.DOB).click()
        sel1 = Select(self.driver.find_element(By.XPATH, self.monthDOB))
        sel1.select_by_visible_text("January")
        sel2 = Select(self.driver.find_element(By.XPATH, self.yearDOB))
        sel2.select_by_visible_text("1980")
        self.driver.find_element(By.XPATH, self.dayDOB).click()

    def input_postcode(self, post_code):
        self.driver.find_element(By.XPATH, self.postCode).click()
        self.driver.find_element(By.XPATH, self.postCode).send_keys(post_code)

    def input_passport_number(self, passport_number):
        self.driver.find_element(By.XPATH, self.passportNumber).click()
        self.driver.find_element(By.XPATH, self.passportNumber).send_keys(passport_number)

    def give_passport_expiry_date(self):
        self.driver.find_element(By.XPATH, self.passportExpiryDateField).click()
        sel1 = Select(self.driver.find_element(By.XPATH, self.passportExpiryMonth))
        sel1.select_by_visible_text("June")
        sel2 = Select(self.driver.find_element(By.XPATH, self.passportExpiryYear))
        sel2.select_by_visible_text("2024")
        self.driver.find_element(By.XPATH, self.passportExpiryDate).click()

    def select_bank(self):
        self.driver.find_element(By.XPATH, self.bank).click()

    def click_quick_pick_checkbox(self):
        self.driver.find_element(By.XPATH, self.quickPickCheckBox).click()

    def click_tc_checkbox(self):
        self.driver.find_element(By.XPATH, self.tcCheckBox).click()

    def click_paynow_button(self):
        self.driver.find_element(By.XPATH, self.paynowButton).click()
















