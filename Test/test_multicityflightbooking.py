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










