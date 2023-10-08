import unittest
from main import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_all_users_data(self):
        response = self.app.get('/api/stats/users?date=2023-27-09-20:00')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"usersOnline": 34})

    def test_get_user_data(self):
        response = self.app.get('/api/stats/user?date=2023-27-09-20:00&userId=A4DC2287-B03D-430C-92E8-02216D828709')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"wasUserOnline": False, "nearestOnlineTime": "2023-28-09-15:00"})

    def test_predict_users_count(self):
        response = self.app.get('/api/predictions/users?date=2025-27-09-20:00')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"onlineUsers": 31})

    def test_predict_user_status(self):
        response = self.app.get('/api/predictions/user?date=2025-27-09-20:00&tolerance=0.85&userId=A4DC2287-B03D-430C-92E8-02216D828709')
        self.assertEqual(response.status_code, 200)
        self.assertIn("willBeOnline", response.json)
        self.assertIn("onlineChance", response.json)