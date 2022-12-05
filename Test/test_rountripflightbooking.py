import random
import string
import time
import unittest
import pytest
from Pages.loginpage import Login
from Pages.onewayflightbooking import OneWayFlight
from Pages.dateforflight import DateForFlights
from Pages.roundtripflightbooking import RoundTripFlight


@pytest.mark.usefixtures("test_setup")
class TestRoundTripFlightBooking(unittest.TestCase):
    def test1_valid_roundtrip_flight_booking(self):
        driver = self.driver
        login_roundtrip_flight_booking = Login(driver)
        login_roundtrip_flight_booking.click_profile_icon_login()
        login_roundtrip_flight_booking.click_login()
        login_roundtrip_flight_booking.enter_email_login("mim@sharetrip.net")
        login_roundtrip_flight_booking.enter_password_login("Vugijugi78")
        login_roundtrip_flight_booking.click_login_button()

        login_roundtrip_flight_booking = RoundTripFlight(driver)
        login_roundtrip_flight_booking.input_flying_from_roundtrip("bkk")
        login_roundtrip_flight_booking.input_flying_to_roundtrip("kua")

        login_roundtrip_flight_booking = DateForFlights(driver)
        login_roundtrip_flight_booking.select_target_date("January 2023", 28)
        login_roundtrip_flight_booking.select_return_date("February 2023", 4)

        login_roundtrip_flight_booking = OneWayFlight(driver)
        # login_roundtrip_flight_booking.click_economy()
        login_roundtrip_flight_booking.click_search_button()
        login_roundtrip_flight_booking.click_cross_button()
        time.sleep(4)
        login_roundtrip_flight_booking.click_book_button()
        login_roundtrip_flight_booking.switch_window()
        login_roundtrip_flight_booking.click_title()
        login_roundtrip_flight_booking.input_given_name(''.join(random.choices(string.ascii_letters, k=10)))
        login_roundtrip_flight_booking.input_sur_name(''.join(random.choices(string.ascii_letters, k=8)))
        login_roundtrip_flight_booking.click_radio_button_earn_tc()
        driver.execute_script("window.scrollTo(0,600)")
        login_roundtrip_flight_booking.input_phone_number(f"{random.randrange(100000000000)}")
        login_roundtrip_flight_booking.select_DOB()
        postcode = f"{random.randrange(10000)}"
        login_roundtrip_flight_booking.input_postcode(postcode)

        def get_random_passport_number(length=1):
            letters = string.ascii_uppercase
            random_string = ''.join(random.choice(letters) for _ in range(length))
            return random_string

        random_passport_number = f"{get_random_passport_number(2)}{random.randrange(1000000)}"
        login_roundtrip_flight_booking.input_passport_number(random_passport_number)
        login_roundtrip_flight_booking.give_passport_expiry_date()
        login_roundtrip_flight_booking.select_bank()
        driver.execute_script("window.scrollTo(0, 600)")
        login_roundtrip_flight_booking.click_quick_pick_checkbox()
        driver.execute_script("window.scrollTo(0, 600)")
        login_roundtrip_flight_booking.click_tc_checkbox()
        # driver.execute_script("window.scrollTo(0, 200")
        login_roundtrip_flight_booking.click_paynow_button()
        time.sleep(4)

        print("Test Case Running Successfully")
