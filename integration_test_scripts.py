import requests
import unittest


class APITest(unittest.TestCase):

    def test_integration_of_service_one(self):
        url_of_service_one = "http://localhost:8101/api"
        data = {'message': 'new message'}
        response = requests.post(url_of_service_one, data)
        expected_response = data.get('message')[::-1]
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('message'), expected_response)
        self.assertEqual(len(response.json()), 2)

    def test_integration_of_service_two(self):
        url_of_service_one = "http://localhost:8102/reverse"
        data = {'message': 'new message'}
        response = requests.post(url_of_service_one, data)
        expected_response = data.get('message')[::-1]
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('message'), expected_response)
        self.assertEqual(len(response.json()), 1)


if __name__ == "__main__":
    api_test = APITest()
    api_test.test_integration_of_service_one()
    api_test.test_integration_of_service_two()
