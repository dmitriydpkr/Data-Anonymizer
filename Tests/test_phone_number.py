import unittest
from views import get_phone_number


class TestPhoneNumber(unittest.TestCase):

    def test_get_phone_number_5(self):
        test_string = 'Lorem +48 845 546 546, +48 777 777 777 sit 898 845 566 amet'
        count_hidden_digits = 5
        masks_char = 'X'
        result = get_phone_number(test_string, count_hidden_digits, masks_char)
        expected = 'Lorem +48 845 5XX XXX, +48 777 7XX XXX sit 898 845 566 amet'
        self.assertEqual(result, expected)

    def test_get_phone_number_1(self):
        test_string = 'Lorem +48 845 546 546, +48 777 777 777 sit 898 845 566 amet'
        count_hidden_digits = 1
        masks_char = 'X'
        result = get_phone_number(test_string, count_hidden_digits, masks_char)
        expected = 'Lorem +48 845 546 54X, +48 777 777 77X sit 898 845 566 amet'
        self.assertEqual(result, expected)

    def test_get_phone_number_0(self):
        test_string = 'Lorem +48 845 546 546, +48 777 777 777 sit 898 845 566 amet'
        count_hidden_digits = 0
        masks_char = 'X'
        result = get_phone_number(test_string, count_hidden_digits, masks_char)
        expected = 'Lorem +48 845 546 546, +48 777 777 777 sit 898 845 566 amet'
        self.assertEqual(result, expected)

    def test_get_phone_number_12(self):
        test_string = 'Lorem +48 845 546 546, +48 777 777 777 sit 898 845 566 amet'
        count_hidden_digits = 13
        masks_char = 'X'
        result = get_phone_number(test_string, count_hidden_digits, masks_char)
        expected = 'Lorem +48 845 546 546, +48 777 777 777 sit 898 845 566 amet'
        self.assertEqual(result, expected)

    def test_get_phone_number_9(self):
        test_string = 'Lorem +48 845 546 546, +48 777 777 777 sit 898 845 566 amet'
        count_hidden_digits = 9
        masks_char = 'X'
        result = get_phone_number(test_string, count_hidden_digits, masks_char)
        expected = 'Lorem +48 XXX XXX XXX, +48 XXX XXX XXX sit 898 845 566 amet'
        self.assertEqual(result, expected)

    def test_get_phone_number_11(self):
        test_string = 'Lorem +48 845 546 546, +48 777 777 777 sit 898 845 566 amet'
        count_hidden_digits = 11
        masks_char = 'X'
        result = get_phone_number(test_string, count_hidden_digits, masks_char)
        expected = 'Lorem +XX XXX XXX XXX, +XX XXX XXX XXX sit 898 845 566 amet'
        self.assertEqual(result, expected)

    def test_get_phone_number_empty_string(self):
        test_string = ''
        count_hidden_digits = 11
        masks_char = 'X'
        result = get_phone_number(test_string, count_hidden_digits, masks_char)
        expected = ''
        self.assertEqual(result, expected)

    def test_get_phone_number_0_empty_string(self):
        test_string = ''
        count_hidden_digits = 0
        masks_char = 'X'
        result = get_phone_number(test_string, count_hidden_digits, masks_char)
        expected = ''
        self.assertEqual(result, expected)

    def test_get_phone_number_wrong_format(self):
        test_string = ''
        count_hidden_digits = 0
        masks_char = 'X'
        result = get_phone_number(test_string, count_hidden_digits, masks_char)
        expected = ''
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
