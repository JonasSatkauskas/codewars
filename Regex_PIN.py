# Regex validate PIN code

'''ATM machines allow 4 or 6 digit PIN codes 
and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.'''

import re


def validate_pin(pin):
    #return true or false
    four_digits_check = re.search("^\d{4}$", str(pin))
    six_digits_check = re.search("^\d{6}$", str(pin))

    if four_digits_check or six_digits_check:
        return True
    else:
        return False    
    
