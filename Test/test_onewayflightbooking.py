import random
import string
import time
import unittest
import pytest
from Pages.loginpage import Login
from Pages.onewayflightbooking import OneWayFlight
from Pages.dateforflight import DateForFlights


@pytest.mark.usefixtures("test_setup")
class TestOneWayFlightBooking(unittest.TestCase):

    def test1_valid_oneway_flight_booking(self):
        driver = self.driver
        login_oneway_flight_booking = Login(driver)
        login_oneway_flight_booking.click_profile_icon_login()
        login_oneway_flight_booking.click_login()
        login_oneway_flight_booking.enter_email_login("mim@sharetrip.net")
        login_oneway_flight_booking.enter_password_login("Vugijugi78")
        login_oneway_flight_booking.click_login_button()
        time.sleep(2)

        oneway_flight = OneWayFlight(driver)
        oneway_flight.click_oneway_tab()
        oneway_flight.input_flying_from_oneway("bkk")
        oneway_flight.input_flying_to_oneway("kua")

        oneway_flight = DateForFlights(driver)
        oneway_flight.select_target_date("January 2023", 21)
        time.sleep(4)

        oneway_flight = OneWayFlight(driver)
        oneway_flight.click_economy()
        oneway_flight.click_search_button()
        time.sleep(2)
        oneway_flight.click_cross_button()
        time.sleep(1)
        oneway_flight.click_book_button()
        time.sleep(4)
        oneway_flight.switch_window()
        print(driver.title)
        time.sleep(4)
        oneway_flight.click_title()
        oneway_flight.input_given_name(''.join(random.choices(string.ascii_letters, k=10)))
        oneway_flight.input_sur_name(''.join(random.choices(string.ascii_letters, k=8)))
        time.sleep(2)
        # oneway_flight.click_radio_button_earn_tc()
        oneway_flight.click_radio_button_redeem_tc()
        time.sleep(4)

        driver.execute_script("window.scrollTo(0, 600)")
        oneway_flight.input_phone_number(f"{random.randrange(100000000000)}")
        oneway_flight.select_DOB()
        postcode = f"{random.randrange(10000)}"
        # postcode = random.randrange(1000,9999) """another way to generate dynamic postcode"""
        oneway_flight.input_postcode(postcode)

        def get_random_passport_number(length=1):
            letters = string.ascii_uppercase
            random_string = ''.join(random.choice(letters) for _ in range(length))
            return random_string
        random_passport_number = f"{get_random_passport_number(2)}{random.randrange(1000000)}"
        oneway_flight.input_passport_number(random_passport_number)
        oneway_flight.give_passport_expiry_date()
        oneway_flight.select_bank()
        driver.execute_script("window.scrollTo(0, 600)")
        oneway_flight.click_quick_pick_checkbox()
        driver.execute_script("window.scrollTo(0, 800)")
        oneway_flight.click_tc_checkbox()
        # oneway_flight.click_paynow_button()
        time.sleep(4)
        print("done successfully")


