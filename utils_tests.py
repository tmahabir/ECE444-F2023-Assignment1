import unittest
from utils import Utils

class TestUtils(unittest.TestCase):
    def test_reversed(self):
        self.assertEqual(Utils.reversed(2468), 8642)
        self.assertEqual(Utils.reversed(7), 7)
        with self.assertRaises(ValueError):
            Utils.reversed("10")
        with self.assertRaises(ValueError):
            Utils.reversed(3.14) 

    def test_formatter(self):
        self.assertEqual(Utils.formatter(10), ('0b1010', '0o12'))
        self.assertEqual(Utils.formatter(42), ('0b101010', '0o52'))
        with self.assertRaises(ValueError):
            Utils.formatter("10")
        with self.assertRaises(ValueError):
            Utils.formatter(3.14) 

if __name__ == '__main__':
    unittest.main()