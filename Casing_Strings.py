'''Your task is to convert strings to how they would be written by Jaden Smith. 
The strings are actual quotes from Jaden Smith, 
but they are not capitalized in the same way he originally typed them.'''

def to_jaden_case(string):
    sepparate_words = string.split()
    final_words = []
    for word in sepparate_words:
        upper_case = word.capitalize()
        final_words.append(upper_case)
    x = ' '.join(final_words)
    return x
          
    
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))