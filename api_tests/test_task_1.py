import unittest
import requests

from api_tests.utils.config_util import get_authorization


class TestSumEndpoint(unittest.TestCase):
    _GET_SUM_ENDPOINT_TEMPLATE = "http://localhost:4000/sum?a={first_value}&b={second_value}"

    # positive test
    def test_sum_with_positive_numbers(self):
        response = self._get_endpoint_response(first_value=3, second_value=11)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 14)

    def test_sum_with_negative_numbers(self):
        response = self._get_endpoint_response(first_value=3, second_value=-11)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], -8)

    def test_sum_with_one_zero_number(self):
        response = self._get_endpoint_response(first_value=0, second_value=11)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 11)

    # negative test
    def test_sum_with_string_value_validation(self):
        response = self._get_endpoint_response(first_value=3, second_value='eleven')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Expected Numeric Param")

    def test_sum_with_decimal_value_validation(self):
        response = self._get_endpoint_response(first_value=3, second_value=11.0)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Expected Numeric Param")

    def test_sum_with_long_value_validation(self):
        response = self._get_endpoint_response(first_value=0, second_value=18446744073709551615)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Expected Numeric Param")

    def test_sum_with_missed_parameter_validation(self):
        authorization_header = get_authorization()

        response = requests.get(
            url="http://localhost:4000/sum?a=1",
            headers=authorization_header
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Missing Param")

    # helpers
    def _get_endpoint_response(self, first_value, second_value):
        authorization_header = get_authorization()
        response = requests.get(
            url=self._GET_SUM_ENDPOINT_TEMPLATE.format(first_value=first_value,
                                                       second_value=second_value),
            headers=authorization_header
        )
        return response
