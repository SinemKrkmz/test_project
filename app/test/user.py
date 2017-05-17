import unittest
from app.api_function.user import ApiUser


# class TestA(unittest.TestCase):
#     def test_abc(self):
#         a = 9
#         b = 3
#         c = a * b
#         self.assertEqual(c, 13, "nonono")

class test_login_panel(unittest.TestCase):
    def panel_login_admin(self):
        res = ApiUser().post_panel_login("system_admin@facekart.com", "5552222222", "123456aA")
        self.assertEquals(200, res.status, "no")
