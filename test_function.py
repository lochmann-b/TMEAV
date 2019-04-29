#Note to run the test type python test_function.py in the terminal window

import unittest

from email_utils import is_email_address_valid


class TestEmailChecker(unittest.TestCase):
    def test_1(self):
        """
        Test if string has no "@" sign result is FALSE
        """
        data = "This string does not contain an 'at' sign"
        result = is_email_address_valid(data)
        self.assertEqual(result, False)
    
    def test_2(self):
        """
        Test if string has exactly one "@" sign but no other email address like components
        result is FALSE
        """
        data = "This string does contain one @ sign"
        result = is_email_address_valid(data)
        self.assertEqual(result, False)
    
    def test_3(self):
        """
        Test something that looks like an email address but has a second 
        @ sign is FALSE
        """
        data = "firstname@lastname@gmail.com"
        result = is_email_address_valid(data)
        self.assertEqual(result, False)
    
    def test_4(self):
        """
        Test firstname.lastname+extra@yahoo.com is TRUE
        """
        data = "firstname.lastname+extra@yahoo.com"
        result = is_email_address_valid(data)
        self.assertEqual(result, True)

    def test_5(self):
        """
        Test firstname.lastname@domain.com is TRUE
        """
        data = "firstname.lastname@domain.edu"
        result = is_email_address_valid(data)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
