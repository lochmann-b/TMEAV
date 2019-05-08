#Note to run the test, type "python -m unittest tests/test_is_email_address_valid.py" in the terminal window

import unittest

from app.main.email_utils import is_email_address_valid, are_email_addresses_valid


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

    def test_email_addresses_separated_by_semicolon_should_pass(self):
        """
        Test semicolon separated emailsare TRUE
        """
        data = "max@test.org;magnus@carlsen.com"
        result = are_email_addresses_valid(data)
        self.assertEqual(result, True)

    def test_incomplete_email_addresses_separated_by_semicolon_should_fail(self):
        """
        Test incomplete email addresses separated are FALSE
        """
        data = "max@test.org;magnus@carlsen"
        result = are_email_addresses_valid(data)
        self.assertEqual(result, False)

    def test_email_address_with_trailing_semicolon_should_fail(self):
        """
        Test email addresse with trailing seimicolon is FALSE
        """
        data = "max@test.org;"
        result = are_email_addresses_valid(data)
        self.assertEqual(result, False)
    
    def test_email_address_with_leading_semicolon_should_fail(self):
        """
        Test email addresse with leading  seimicolon is FALSE
        """
        data = ";max@test.org"
        result = are_email_addresses_valid(data)
        self.assertEqual(result, False)
    
    def test_single_email_address_should_pass(self):
        """
        Single email address is TRUE
        """
        data = "max@test.org"
        result = are_email_addresses_valid(data)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
