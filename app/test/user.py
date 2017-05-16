import unittest

class TestA(unittest.TestCase):
    def test_abc(self):
        a = 9
        b = 3
        c = a * b
        self.assertEqual(c, 13, "nonono")
