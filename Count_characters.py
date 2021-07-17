"""The main idea is to count all the occurring characters in a string. 
If you have a string like aba, then the result should be {'a': 2, 'b': 1}."""

from collections import Counter

def count(string):
    # Separate each character
    empty_dict = {}
    if len(string) >= 1:
        for i in string:
            counter = Counter(string)
            letters = counter[i]
            empty_dict[i] = letters

        return empty_dict
    else:
        return {}

print(count('abcda'))