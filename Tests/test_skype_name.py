import unittest
from views import get_skype_name


class TestSkypeName(unittest.TestCase):

    def test_get_skype_name_html(self):
        test_string = 'Lorem ipsum <a href=”skype:loremipsum?call”>call</a>,dolor sit)'
        masks_char = '*'
        result = get_skype_name(test_string, masks_char)
        expected = 'Lorem ipsum <a href=”skype:*?call”>call</a>,dolor sit)'
        self.assertEqual(result, expected)

    def test_get_skype_name_lower(self):
        test_string = 'skype:username'
        masks_char = '#'
        result = get_skype_name(test_string, masks_char)
        expected = 'skype:#'
        self.assertEqual(result, expected)

    def test_get_skype_name_upper(self):
        test_string = 'skype:USERNAME'
        masks_char = '#'
        result = get_skype_name(test_string, masks_char)
        expected = 'skype:#'
        self.assertEqual(result, expected)

    def test_get_skype_name_without_skype(self):
        test_string = 't)'
        masks_char = '#'
        result = get_skype_name(test_string, masks_char)
        expected = 't)'
        self.assertEqual(result, expected)

#
# if __name__ == '__main__':
#     unittest.main()
