import unittest
from views import get_email


class TestEmail(unittest.TestCase):

    def test_get_email(self):
        test_string = 'john.doe@gmail.com'
        result = get_email(test_string, '*')
        expected = 'j*******e@gmail.com'
        self.assertEqual(result, expected)

    def test_get_email_with_symbol_1(self):
        test_string = 'Lorem abc-abc@abc.edu.co.uk am'
        result = get_email(test_string, '*')
        expected = 'Lorem a******c@abc.edu.co.uk am'
        self.assertEqual(result, expected)

    def test_get_email_with_symbol_2(self):
        test_string = 'john.doe@gmail.com'
        result = get_email(test_string, '*')
        expected = 'j*******e@gmail.com'
        self.assertEqual(result, expected)

    def test_get_email_with_symbol_3(self):
        test_string = 'john+doe@gmail.com'
        result = get_email(test_string, '*')
        expected = 'j*******e@gmail.com'
        self.assertEqual(result, expected)

    def test_get_email_with_symbol_4(self):
        test_string = 'john_doe@gmail.com'
        result = get_email(test_string, '*')
        expected = 'j*******e@gmail.com'
        self.assertEqual(result, expected)

    def test_get_email_with_wrong_symbol(self):
        test_string = 'Lorem abc//abc@abc.edu.co.uk am'
        result = get_email(test_string, '*')
        expected = 'Lorem abc//abc@abc.edu.co.uk am'
        self.assertEqual(result, expected)

    def test_get_email_with_wrong_format(self):
        test_string = 'Lorem abcabc@abc.edu.co.uk am'
        result = get_email(test_string, '*')
        expected = 'Lorem abcabc@abc.edu.co.uk am'
        self.assertEqual(result, expected)

    def test_get_email_without_data(self):
        test_string = 'Lorem ipsum --@--.--'
        result = get_email(test_string, '*')
        expected = 'Lorem ipsum --@--.--'
        self.assertEqual(result, expected)

    def test_get_email_with_wrong_first_symbol_of_username(self):
        test_string = '/john.doe@gmail.com'
        result = get_email(test_string, '*')
        expected = '/john.doe@gmail.com'
        self.assertEqual(result, expected)

    def test_get_email_with_wrong_last_symbol_of_username(self):
        test_string = 'john.doe+@gmail.com'
        result = get_email(test_string, '*')
        expected = 'john.doe+@gmail.com'
        self.assertEqual(result, expected)

    def test_get_email_with_wrong_first_symbol_of_domain(self):
        test_string = '/john.doe@#gmail.com'
        result = get_email(test_string, '*')
        expected = '/john.doe@#gmail.com'
        self.assertEqual(result, expected)

    def test_get_email_with_wrong_last_symbol_of_domain(self):
        test_string = 'john.doe@gmail.com#'
        result = get_email(test_string, '*')
        expected = 'john.doe@gmail.com#'
        self.assertEqual(result, expected)


# if __name__ == '__main__':
#     unittest.main()
