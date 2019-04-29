from xml.sax import make_parser, handler
from check_email_address_function import check_email_address

class CustomerHandler(handler.ContentHandler):

    def __init__(self):
        self.invalid_lines = []
        self.current_column = -1
        self.current_name = ''
        self.current_email = ''

    def startElement(self, name, attrs):
        if name == 'Row':
            self.current_column = -1
            self.current_name = ''
            self.current_email = ''
        elif name == 'Cell':
            self.current_column += 1

    def characters(self, content):
        if self.current_column == 0:
            self.current_name += content.strip()
        elif self.current_column == 1:
            self.current_email += content.strip()

    def is_valid_line(self):
        #incomplete lines are considered as valid
        if self.current_name and self.current_email:
            return check_email_address(self.current_email)
        return True


    def endElement(self, name):
        if name == "Row":
         if not self.is_valid_line():
            self.invalid_lines.append((self.current_name, self.current_email))

    def get_invalid_lines(self):
        return self.invalid_lines

def check_email_addresses(file):
    parser = make_parser()
    cust_handler = CustomerHandler()
    parser.setContentHandler(cust_handler)
    parser.parse(file)
    for line in cust_handler.get_invalid_lines():
        print(line)