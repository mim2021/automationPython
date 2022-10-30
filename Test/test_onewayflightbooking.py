import time
import unittest
import pytest
from Pages.loginpage import Login
from Pages.onewayflightbooking import OneWayFlight


@pytest.mark.usefixtures("test_setup")
class TestOneWayFlightBooking(unittest.TestCase):

    def test1_valid_oneway_flight_booking(self):
        driver = self.driver
        login_oneway_flight_booking = Login(driver)
        login_oneway_flight_booking.click_profile_icon_login()
        login_oneway_flight_booking.click_login()
        login_oneway_flight_booking.enter_email_login("mim@sharetrip.net")
        login_oneway_flight_booking.enter_password_login("vugijugi")
        login_oneway_flight_booking.click_login_button()
        time.sleep(2)

        oneway_flight = OneWayFlight(driver)
        oneway_flight.click_oneway_tab()
        oneway_flight.input_flying_from_oneway("bkk")
        time.sleep(4)
        oneway_flight.input_flying_to_oneway("kua")
        time.sleep(4)
        oneway_flight.click_select_date_oneway()
        time.sleep(4)
        oneway_flight.click_arrow()
        time.sleep(4)
        oneway_flight.click_date()
        print("done successfully")
        time.sleep(4)
