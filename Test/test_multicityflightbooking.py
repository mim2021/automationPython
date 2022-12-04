import random
import string
import time
import unittest
import pytest
from Pages.loginpage import Login
from Pages.multicityflightbooking import MultiCityFlight
from Pages.dateforflight import DateForFlights
from Pages.onewayflightbooking import OneWayFlight


@pytest.mark.usefixtures("test_setup")
class TestMultiCityFlightBooking(unittest.TestCase):

    def test1_valid_multi_city_flight_booking(self):
        driver = self.driver
        login_multi_city_flight_booking = Login(driver)
        login_multi_city_flight_booking.click_profile_icon_login()
        login_multi_city_flight_booking.click_login()
        login_multi_city_flight_booking.enter_email_login("mim@sharetrip.net")
        login_multi_city_flight_booking.enter_password_login("Vugijugi78")
        login_multi_city_flight_booking.click_login_button()

        multi_city_flight = MultiCityFlight(driver)
        multi_city_flight.click_multi_city_tab()
        multi_city_flight.input_multi_city_flying_from1("dac")
        multi_city_flight.input_multi_city_flying_to1("bkk")

        multi_city_flight_date1 = DateForFlights(driver)
        multi_city_flight_date1.select_target_date("January 2023", 21)
        time.sleep(2)

        multi_city_flight.input_multi_city_flying_from2("bkk")
        multi_city_flight.input_multi_city_flying_to2("sin")

        multi_city_flight_date1 = DateForFlights(driver)
        multi_city_flight_date1.select_target_date2("January 2023", 27)
        time.sleep(2)

        multi_city_flight.add_city_1()
        multi_city_flight.input_multi_city_flying_from3("sin")
        multi_city_flight.input_multi_city_flying_to3("dac")

        multi_city_flight_date1 = DateForFlights(driver)
        multi_city_flight_date1.select_target_date3("February 2023", 2)
        time.sleep(2)

        multi_city_flight.click_search_button()
        time.sleep(2)

        multi_city_flight_details = OneWayFlight(driver)
        multi_city_flight_details.click_cross_button()
        multi_city_flight_details.click_book_button()
        multi_city_flight_details.switch_window()
        print(driver.title)
        time.sleep(2)
        multi_city_flight_details.click_title()
        time.sleep(2)
        multi_city_flight_details.input_given_name(''.join(random.choices(string.ascii_letters, k=10)))
        multi_city_flight_details.input_sur_name(''.join(random.choices(string.ascii_letters, k=8)))
        multi_city_flight_details.click_radio_button_earn_tc()
        driver.execute_script("window.scrollTo(0,600)")
        multi_city_flight_details.input_phone_number(f'{random.randrange(100000000000)}')
        multi_city_flight_details.select_DOB()
        postcode = random.randrange(1000, 9999)
        multi_city_flight_details.input_postcode(postcode)

        def get_random_passport_number(length=1):
            letters = string.ascii_uppercase
            random_string = ''.join(random.choice(letters) for _ in range(length))
            return random_string
        random_passport_number = f'{get_random_passport_number(2)}{random.randrange(1000000)}'
        multi_city_flight_details.input_passport_number(random_passport_number)
        multi_city_flight_details.give_passport_expiry_date()
        multi_city_flight_details.select_bank()
        driver.execute_script("window.scrollTo(0, 600)")
        multi_city_flight_details.click_quick_pick_checkbox()
        driver.execute_script("window.scrollTo(0, 600)")
        multi_city_flight_details.click_tc_checkbox()
        # multi_city_flight_details.click_paynow_button()
        time.sleep(4)
        print("Test Case Running Successfully")
















