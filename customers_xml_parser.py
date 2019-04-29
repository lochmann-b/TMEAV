from xml.sax import make_parser, handler
from email_utils import is_email_address_valid

class CustomerHandler(handler.ContentHandler):

    def __init__(self):
        self.invalid_lines = [] #used to collect the invalid lines
        self.current_column = -1 #current column beeing parsed. 0 = name, 1 = email address, -1 = none
        self.current_name = '' # name found in current line
        self.current_email = '' # email address found in current line

    def startElement(self, name, attrs):
        if name == 'Row':
            # we are at the start of a row.
            # reset row related stuff
            self.current_column = -1
            self.current_name = ''
            self.current_email = ''
        elif name == 'Cell':
            # we are at the start of a column.
            # increase column index
            self.current_column += 1

    def characters(self, content):
        # we now are extracting content found between a a start tag and an end tag
        # please note that this method could be called multiple times for the same start/end tag.
        # Therefore, the content as to be appended to the current name/email address

        if self.current_column == 0:
            # append content of first column to current_name
            self.current_name += content.strip()
        elif self.current_column == 1:
            # append content of second column to current_email
            self.current_email += content.strip()

    def is_valid_line(self):
        #incomplete lines are considered as valid
        if self.current_name and self.current_email:
            return is_email_address_valid(self.current_email)
        return True

    def endElement(self, name):
        # we hit the end of a row.
        # check if the collected name / email address should be considered as invalid
        if name == "Row":
         if not self.is_valid_line():
            self.invalid_lines.append((self.current_name, self.current_email))

    def get_invalid_lines(self):
        return self.invalid_lines

def check_email_addresses(file):
    """Scans the xml file for invalid email addresses.
       Only lines containing both a name and an email will be considered.

    Parameters
    ----------
    file : str
        the xml file to parse

    Returns
    -------
    list
        a list of tuples representing the lines where invalid email addreses have been found.        
    """
    parser = make_parser()
    cust_handler = CustomerHandler()
    parser.setContentHandler(cust_handler)
    parser.parse(file)
    return cust_handler.get_invalid_lines()
    