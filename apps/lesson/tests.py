from django.test import TestCase, Client
from rest_framework.test import APIClient
from apps.lesson.models.lesson import Lesson

class UserTest(TestCase):
  client = APIClient()
  fixtures = ['seed.json']

  def test_user_fail(self):
    submit_response = self.client.post('/api/lessons/1/submit/', 
      data={
      "answers": {
        "2": ["3"],
        "6": ["7"]
      },
      "username": "user_pass" ,
    }, format="json", content_type="application/json; charset=utf-8")

    self.assertEqual(submit_response.status_code, 200)
    self.assertEqual(submit_response.data['result'], 'Fail')

  def test_user_pass(self):
    submit_response = self.client.post('/api/lessons/1/submit/', 
      data={
      "answers": {
        "2": ["3", "4"],
        "6": ["7"]
      },
      "username": "user_pass" ,
    }, format="json", content_type="application/json; charset=utf-8")

    self.assertEqual(submit_response.status_code, 200)
    self.assertEqual(submit_response.data['result'], 'Pass')


