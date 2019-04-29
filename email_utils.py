import re

# function to check email address
def is_email_address_valid(email_address):
    #regex copied from https://emailregex.com/
    regexp = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    return regexp.match(email_address) != None
