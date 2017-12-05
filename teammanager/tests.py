
from rest_framework.test import APIClient
import unittest


class Members(unittest.TestCase):
	def test(self):
		client = APIClient()
		response = client.get('/api/members/')
		self.assertEqual(response.status_code,200)
		user_data = {"first_name": "Jane","last_name": "Doe","phoneno": "8281958680",
		"email": "janedoe1@gmail.com","role": "Regular"}
		response = client.post('/api/members/', user_data, format='json')
		self.assertEqual(response.status_code,201)
		user_data["phoneno"] = "+918281958680"
		response = client.patch('/api/members/1/', user_data, format='json')
		self.assertEqual(response.status_code,200)