import time
import unittest
import requests

from api_tests.utils.config_util import get_authorization


class TestSumLazyEndpoint(unittest.TestCase):
    _GET_SUM_LIMITED_ENDPOINT_TEMPLATE = "http://localhost:4000/sumLimited?a=1&b=2"

    # positive test
    def test_sum_limited_with_positive_timeout(self):
        time.sleep(1)
        response = self._get_endpoint_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 3)
        time.sleep(1)
        response = self._get_endpoint_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 3)

    # negative test
    def test_sum_limited_with_negative_timeout(self):
        time.sleep(1)
        response = self._get_endpoint_response()
        self.assertEqual(response.status_code, 200)
        time.sleep(0.5)
        response = self._get_endpoint_response()
        self.assertEqual(response.status_code, 429)
        self.assertEqual(response.json()["error"], "Too Many Requests")

    # helpers
    def _get_endpoint_response(self):
        authorization_header = get_authorization()
        response = requests.get(
            url=self._GET_SUM_LIMITED_ENDPOINT_TEMPLATE,
            headers=authorization_header
        )
        return response
