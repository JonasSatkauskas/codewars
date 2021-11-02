"""
TASK:
You are going to be given a word. 
Your job is to return the middle character of the word. 
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.
"""


def get_middle(word):
    if len(word) % 2 == 0:
        offset = int(len(word) / 2)
        return word[offset - 1 : offset + 1]
    else:
        offset = int(len(word) / 2)
        return word[offset : offset + 1]


print(get_middle("sveika"))
print(get_middle("sveikas"))
