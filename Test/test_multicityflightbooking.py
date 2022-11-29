import time
import unittest
import pytest
from Pages.loginpage import Login
from Pages.multicityflightbooking import MultiCityFlight
from Pages.dateforflight import DateForFlights


@pytest.mark.usefixtures("test_setup")
class TestMultiCityFlightBooking(unittest.TestCase):

    def test1_valid_multicity_flight_booking(self):
        driver = self.driver
        login_multicity_flight_booking = Login(driver)
        login_multicity_flight_booking.click_profile_icon_login()
        login_multicity_flight_booking.click_login()
        login_multicity_flight_booking.enter_email_login("mim@sharetrip.net")
        login_multicity_flight_booking.enter_password_login("Vugijugi78")
        login_multicity_flight_booking.click_login_button()

        multicity_flight = MultiCityFlight(driver)
        multicity_flight.click_multi_city_tab()
        multicity_flight.input_multi_city_flying_from1("dac")
        multicity_flight.input_multi_city_flying_to1("bkk")
        time.sleep(4)
        multicity_flight.input_multi_city_flying_from2("bkk")
        multicity_flight.input_multi_city_flying_to1("sin")
        time.sleep(4)
        multicity_flight.input_multi_city_flying_from3("sin")
        multicity_flight.input_multi_city_flying_to1("dac")
        time.sleep(4)


