"""Your task is to write a function that takes a string
and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become 
"Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.
"""
import re


def disemvowel(string_):
    patterm = r'[aeiouAEIOU]'
    modified_string = re.sub(patterm, '', string_)
    return modified_string

print(disemvowel('I will try to make it easy'))
