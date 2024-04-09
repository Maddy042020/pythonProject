
import json
from src.constants.api_constants import API_Constants
from src.helpers.api_request_wrapper import post_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import create_booking
from src.utils.utils import Util
import pytest
import allure
class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify Createbooking status code should not be null")
    @allure.description("Create a booking and status code should be 200")
    @staticmethod
    def test_create_booking_positive():
        response = post_request(url=API_Constants.create_booking(),auth=None,
                                 headers=Util.common_headers_json(),payload=create_booking(),in_json=False)

        booking_id = response.json()["bookingid"]


        verify_https_code(response_data=response,expected_data=200)
        verify_json_key_for_not_null(booking_id)