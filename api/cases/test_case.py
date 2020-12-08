import unittest
import requests
from celery import shared_task
from seldom import data
import xmlrunner


class Data:
    data_list = []


class Test(unittest.TestCase):

    @data(["1", "2"])
    def test_case(self, number):
        print("-->", number)
        r = requests.get('https://api.github.com/events')
        self.assertEqual(r.status_code, 200)
