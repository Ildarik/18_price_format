import unittest
from format_price import format_price

class TestFormatPrice(unittest.TestCase):

    def test(self):
        self.assertEqual(format_price(3245.000000), '3 245')

if __name__ == '__main__':
    unittest.main()