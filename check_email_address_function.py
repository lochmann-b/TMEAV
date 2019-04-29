# function to check email address
def check_email_address(email_address):
    """This function takes an string input and checks if there is exactly one '@'' sign and at least one '.' 
    to ensure the user did not enter something else than an email address by mistake"""
    
    import re
    #regexp = re.compile(r"[^@]+@[^@]+\.[^@]+") This was a first test regex not very good
    regexp = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if regexp.search(email_address):
        return 'This is likely an email address'
    else:
        return 'This is not an email address'