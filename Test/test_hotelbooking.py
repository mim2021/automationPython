import time
import unittest
import pytest
from Pages.loginpage import Login
from Pages.hotelbooking import HotelBooking
from Pages.dateforhotel import DateForHotels


@pytest.mark.usefixtures("test_setup")
class TestHotelBooking(unittest.TestCase):

    def test1_valid_hotel_booking(self):
        driver = self.driver
        login_for_hotel_booking = Login(driver)
        login_for_hotel_booking.click_profile_icon_login()
        login_for_hotel_booking.click_login()
        login_for_hotel_booking.enter_email_login("mim@sharetrip.net")
        login_for_hotel_booking.enter_password_login("Vugijugi7")
        login_for_hotel_booking.click_login_button()

        hotel_booking = HotelBooking(driver)
        hotel_booking.click_hotel_tab()
        hotel_booking.enter_city_input("bali")
        time.sleep(4)

        date_hotel_booking = DateForHotels(driver)
        date_hotel_booking.select_target_date("January 2023", 28)
        date_hotel_booking.select_return_date("February 2023", 3)
        time.sleep(4)

        print("Test is running successfully")




