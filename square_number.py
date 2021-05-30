import math

def is_square(n):
    if n < 0:
        return False
    elif len(str(math.sqrt(n))) < 4:
        return True   
    else:
        return False
        

print(is_square(-1))
