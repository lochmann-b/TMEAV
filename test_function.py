import unittest

from check_email_address_function import check_email_address


class TestEmailChecker(unittest.TestCase):
    def test_1(self):
        """
        Test if string has no "@" sign result is FALSE
        """
        data = "This string does not contain an 'at' sign"
        result = check_email_address(data)
        self.assertEqual(result, 'This is not an email address')
    
    def test_2(self):
        """
        Test if string has exactly one "@" sign but no other email address like components
        result is FALSE
        """
        data = "This string does contain one @ sign"
        result = check_email_address(data)
        self.assertEqual(result, 'This is not an email address')
    
    def test_3(self):
        """
        Test something that looks like an email address but has a second 
        @ sign is FALSE
        """
        data = "firstname@lastname@gmail.com"
        result = check_email_address(data)
        self.assertEqual(result, 'This is not an email address')
    
    def test_4(self):
        """
        Test firstname.lastname+extra@yahoo.com is TRUE
        """
        data = "firstname.lastname+extra@yahoo.com"
        result = check_email_address(data)
        self.assertEqual(result, 'This is likely an email address')

    def test_5(self):
        """
        Test firstname.lastname@domain.com is TRUE
        """
        data = "firstname.lastname@domain.edu"
        result = check_email_address(data)
        self.assertEqual(result, 'This is likely an email address')

if __name__ == '__main__':
    unittest.main()
