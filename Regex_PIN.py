# Regex validate PIN code

'''ATM machines allow 4 or 6 digit PIN codes 
and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.'''

import re


def validate_pin(pin=str):
    #return true or false
    listas = []
    for i in str(pin):
        listas.append(i) 
        if listas[0] == '0':
            listas.insert(1, 'o')
            final = ''.join(listas)
            return True

    four_digits_check = re.search("^\d{4}$", str(pin))
    six_digits_check = re.search("^\d{6}$", str(pin))

    if four_digits_check == "1234":
        return False

    elif len(str(pin)) > 4:
        return False

    elif four_digits_check or six_digits_check:
        return True

    else:
        return False    
    

print(validate_pin('098765'))

# training = 9876

# sarasas = str(training)
# listas = []
# for i in sarasas:
#     listas.append(i) 
# listas.insert(1, 'x')
# print(listas)
# final = ''.join(listas)
# print(final)