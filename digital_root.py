''' Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer. '''



def digital_root(n):
    suma = 0
    skaiciu_listas = [int(d) for d in str(n)]
    for skaicius in range(0, len(skaiciu_listas)):
        suma = suma + skaiciu_listas[skaicius]

    if len(str(suma)) > 1:
        galutine = 0
        sarasas = [int(b) for b in str(suma)]

        for number in range(0, len(sarasas)):
            galutine = galutine + sarasas[number]
        return galutine

    else:
        return suma






print(digital_root(493193))


# suma = 0

# sarasas = [1,2,3,4,5]

# for num in range(0, len(sarasas)):
#     suma = suma + sarasas[num]

# print(suma)




