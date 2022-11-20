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
        login_roundtrip_flight_booking.select_target_date("January 2023", 21)
        login_roundtrip_flight_booking.select_return_date("January 2023", 25)





        print("Test Case Running Successfully")
