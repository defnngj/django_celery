import unittest
import requests
from parameterized import parameterized


def interface_data():
    """
    定义接口数据
    """
    data_list = [
        ("http://httpbin.org/get", "get", {"params": {'key': 'value'} }, "resp"),
        ("http://httpbin.org/post", "post", {"data":{'key': 'value'}}, "resp"),
    ]
    return data_list


class Test(unittest.TestCase):
    """
    接口测试用例
    """
    @parameterized.expand(interface_data)
    def test_case(self, url, method, params, resp):
        print("url", url)
        print("-->", method)
        print("-->", params)
        print("-->", resp)
        if method == "get":
            r = requests.get(url, params=params)
            self.assertEqual(r.status_code, 200)
        if method == "post":
            r = requests.post(url, data=params)
            self.assertEqual(r.status_code, 200)
