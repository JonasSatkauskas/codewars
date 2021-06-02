'''Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. The string can contain any char.'''

import re

def xo(s):
    # Finding x's in the given string
    x_findings = re.findall('x', s.lower())
    # Counting how many 'x' letters there are
    x_count = len(x_findings)

    # Finding o's in the given string
    o_findings = re.findall('o', s.lower())
    # Counting how many 'o' letters there are
    o_count = len(o_findings)

    # Checking final condition
    if x_count == o_count:
        return True
    else:
        return False

print(xo('xooxx'))