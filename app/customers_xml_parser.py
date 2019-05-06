from xml.sax import make_parser
from app.email_utils import are_email_addresses_valid
from app.CustomerHandler import CustomerHandler

def is_invalid_line(current_name, current_email):
    #incomplete lines are considered as valid
    if current_name and current_email:
        return not are_email_addresses_valid(current_email)
    return False

def is_valid_line(current_name, current_email):
    #incomplete lines are considered as valid
    if current_name and current_email:
        return are_email_addresses_valid(current_email)
    return False

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
    cust_handler = CustomerHandler(lambda name, e_mail: is_invalid_line(name, e_mail))
    parser.setContentHandler(cust_handler)
    parser.parse(file)
    return cust_handler.get_invalid_lines()

    def chunks(l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

def split_email_addresses(file, chunk_size):
    parser = make_parser()
    cust_handler = CustomerHandler(lambda name, e_mail: is_valid_line(name, e_mail))
    parser.setContentHandler(cust_handler)
    parser.parse(file)
    
    l = cust_handler.get_invalid_lines()
    return [r";".join(map(lambda x: x[1], l[i:i + chunk_size])) for i in range(0, len(l), chunk_size)]