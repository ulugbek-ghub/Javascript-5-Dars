import unittest
from app import son_katta, son_kam
class TestSonMax(unittest.TestCase):
    def test_son(self):
        self.assertEqual(son_katta(8,9,1),9)
    def test_son(self):
        self.assertEqual(son_kam(8,9,1),1)
        self.assertEqual(son_kam(123,238,571), 123)

unittest.main()