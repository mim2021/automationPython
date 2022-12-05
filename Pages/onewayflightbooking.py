import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class OneWayFlight:
    def __init__(self, driver):
        self.driver = driver
        self.onewayTab = "//button[normalize-space()='One Way']"
        self.flyingFromOneWay = "//body/div[@id='__next']/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]"
        self.flyingToOneWay = "//div[@class='icon-input-block search-group circle-left']//div[@class='text-field']//div//input[@id='autocompleteundefined']"
        self.economyClass = "//button[normalize-space()='Economy Class']"
        self.searchButton = "//button[normalize-space()='Search Flights']"
        self.bookButton = "//body/div[@id='__next']/div[1]/section[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[3]/a[1]/button[1]"
        self.title = "//body/div[@id='__next']/div[1]/section[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]"
        self.msTitle = "//body/div[@id='menu-titleName']/div[3]/ul[1]/li[2]"
        self.givenNameField = "givenName"
        self.surNameField = "//input[@name='surName']"
        self.crossButton = "//span[@class='cc-57dy cc-c2rb']"
        self.radioButtonEarnTc = "//span[normalize-space()='I want to Earn Trip Coin']"
        self.radioButtonRedeemTc = "(//span[normalize-space()='I want to Redeem TripCoins'])[1]"
        self.slider = "//span[@class='MuiSlider-thumb MuiSlider-thumbColorPrimary MuiSlider-thumbSizeMedium mui-style-1iua5vb']"
        self.radioButtonCouponCode = "//span[normalize-space()='I want to use Coupon Code']"
        self.couponBox = "//input[@placeholder='Enter Coupon Code']"
        self.phoneNumberField = "//input[@name='mobileNumber']"
        self.dOB = "//*[@id='__next']/div/section/div/div/div[1]/div[2]/div/div/form/section/div[1]/div[4]/div[3]/div/div/div/div[1]/div/div/div/input"
        self.monthDOB = "//select[@class='react-datepicker__month-select']"
        self.yearDOB = "//select[@class='react-datepicker__year-select']"
        self.dayDOB = "//div[@aria-label='Choose Friday, January 18th, 1980']"
        self.postCode = "//input[@name='postCode']"
        self.passportNumber = "//input[@name='passportNumber']"
        self.bank = "//label[@for='inlineRadio1']"
        self.quickPickCheckBox = "//input[@name='quickPick']"
        self.tcCheckBox = "//input[@name='checkedB']"
        self.passportExpiryDateField = "//*[@id='__next']/div/section/div/div/div[1]/div[2]/div/div/form/section/div[1]/div[4]/div[7]/div/div/div/div[1]/div/div/div/input"
        self.passportExpiryMonth = "//select[@class='react-datepicker__month-select']"
        self.passportExpiryYear = "//select[@class='react-datepicker__year-select']"
        self.passportExpiryDate = "//div[@aria-label='Choose Wednesday, June 19th, 2024']"
        self.paynowButton = "//button[normalize-space()='Pay now']"

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

    def click_economy(self):
        self.driver.find_element(By.XPATH, self.economyClass).click()

    def click_search_button(self):
        source = self.driver.find_element(By.XPATH, self.searchButton)
        self.driver.execute_script("arguments[0].click();", source)

    def click_cross_button(self):
        self.driver.find_element(By.XPATH, self.crossButton).click()

    def click_book_button(self):
        book_button = self.driver.find_element(By.XPATH, self.bookButton)
        book_button.click()
        # self.driver.execute_script("arguments[0].click();", book_button)

    def switch_window(self):
        driver = self.driver
        current_window = driver.window_handles[1]
        driver.switch_to.window(current_window)

        """another way"""
        # p = driver.current_window_handle
        # print(driver.current_window_handle)
        # chwd = driver.window_handles
        # for w in chwd:
        #     # switch focus to child window
        #     if w != p:
        #         driver.switch_to.window(w)
        #     break
        # print(driver.window_handles)

    def click_title(self):
        self.driver.find_element(By.XPATH, self.title).click()
        self.driver.find_element(By.XPATH, self.msTitle).click()

    def input_given_name(self, given_name):
        self.driver.find_element(By.NAME, self.givenNameField).click()
        self.driver.find_element(By.NAME, self.givenNameField).send_keys(given_name)

    def input_sur_name(self, sur_name):
        actions = ActionChains(self.driver)
        ele = self.driver.find_element(By.XPATH, self.surNameField)
        actions.move_to_element(ele).click().key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        ele.send_keys(sur_name)

    def click_radio_button_earn_tc(self):
        self.driver.find_element(By.XPATH, self.radioButtonEarnTc).click()

    def click_radio_button_redeem_tc(self):
        self.driver.find_element(By.XPATH, self.radioButtonRedeemTc).click()
        actions = ActionChains(self.driver)
        ele1 = self.driver.find_element(By.XPATH, self.slider)
        self.driver.execute_script("arguments[0].click();", ele1)
        # actions.drag_and_drop_by_offset(ele1, 20, 0).perform()
        actions.click_and_hold(ele1).move_by_offset(20, 0).perform()

    # def enter_coupon(self, coupon_code):
    #     self.driver.find_element(By.XPATH, self.radioButtonCouponCode).click()

    def input_phone_number(self, mobile_number):
        actions = ActionChains(self.driver)
        ele = self.driver.find_element(By.XPATH, self.phoneNumberField)
        actions.move_to_element(ele).click().key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        ele.send_keys(mobile_number)

    def select_DOB(self):
        self.driver.find_element(By.XPATH, self.dOB).click()
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
















