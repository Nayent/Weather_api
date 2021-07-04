import unittest
import requests

from lib import percent, get_data
from app import app


class TestLib(unittest.TestCase):
    def test_percent(self):
        self.assertEqual(percent(10), 5.99)
        self.assertEqual(percent(167), 100.00)


class TestApi(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/"
    ID = '?id=1'

    def test_getData_withow_id(self):
        r = requests.get(TestApi.API_URL)
        self.assertEqual(r.status_code, 400)
    

    def test_getData_with_id(self):
        r = requests.get(TestApi.API_URL + TestApi.ID)
        self.assertEqual(r.status_code, 200)
    

    def test_postData_withow_id(self):
        r = requests.post(TestApi.API_URL)
        self.assertEqual(r.status_code, 400)
    

    def test_postData_with_id(self):
        r = requests.post(TestApi.API_URL + TestApi.ID)
        self.assertEqual(r.status_code, 400)


if __name__ == '__name__':
    unittest.main()