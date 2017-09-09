import unittest
from format_price import format_price

class TestFormatPrice(unittest.TestCase):

    def test_float(self):
        self.assertEqual(format_price(3245.000000), '3 245')

    def test_string(self):
        self.assertEqual(format_price('price'), 'Not available!')

    def test_integer(self):
        self.assertEqual(format_price('119203'), '119 203')

    def test_zero(self):
        self.assertEqual(format_price('0'), 'Price must be greater then 0!')

    def test_negative_value(self):
        self.assertEqual(format_price('-113'), 'Price must be greater then 0!')

    def test_none(self):
        self.assertEqual(format_price(None), 'Not available!')

    def test_list(self):
        self.assertEqual(format_price([99, 199, 24534]), 'Not available!')


if __name__ == '__main__':
    unittest.main()