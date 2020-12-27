import unittest
import requests
from parameterized import parameterized
from api.cases.config import RunConfig


class Test(unittest.TestCase):
    """
    接口测试用例
    """
    @parameterized.expand(RunConfig.data)
    def test_case(self, url, method, params, resp):
        if method == "get":
            r = requests.get(url, params=params)
            self.assertEqual(r.status_code, 200)
        if method == "post":
            r = requests.post(url, data=params)
            self.assertEqual(r.status_code, 200)
