""" Given a string str, reverse it omitting all non-alphabetic characters.
Example

For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".
Input/Output

    [input] string str

A string consists of lowercase latin letters, digits and symbols.

    [output] a string
"""
import re


def reverse_letter(string):
    if string.isalpha():
        return string[::-1]
    else:
        regex = re.findall('[^1,2,3,4,5,6,7,8,9,0,\W]', string)
        first_stop = ''.join(regex)
        regex2 = re.findall('[^_]', first_stop)
        result = ''.join(regex2)
        return result[::-1]


print(reverse_letter('Hell89_o'))