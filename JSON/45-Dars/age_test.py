import unittest
from app import get_age
class AgeTest(unittest.TestCase):
    def test_get_age(self):
        formattest_age = get_age(15)
        self.assertEqual(formattest_age, "Siz 2010-yilda tug'ilgansiz")

unittest.main()