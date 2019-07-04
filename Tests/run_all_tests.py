from unittest import TestLoader, TextTestRunner, TestSuite
from Tests.test_email import TestEmail
from Tests.test_phone_number import TestPhoneNumber
from Tests.test_skype_name import TestSkypeName


loader = TestLoader()
tests = [
    loader.loadTestsFromTestCase(test)
    for test in (TestEmail, TestPhoneNumber, TestSkypeName)
]
suite = TestSuite(tests)

runner = TextTestRunner(verbosity=2)
runner.run(suite)