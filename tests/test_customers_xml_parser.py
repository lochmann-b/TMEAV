#Note to run the test, type "python -m unittest tests/test_customers_xml_parser.py" in the terminal window

import unittest

from app.main.customers_xml_parser import check_email_addresses


class TestCostomersXMLParser(unittest.TestCase):
    def test_check_email_addresses(self):
        file_path = "tests/sampleCustomers.xml"
        result = check_email_addresses(open(file_path, "r"))
        self.assertEqual(result,  [('Name', 'email'), ('Arthur Dent', '42@betelgeuse')])

if __name__ == '__main__':
    unittest.main()
