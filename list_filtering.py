'''In this kata you will create a function 
that takes a list of non-negative integers and strings 
and returns a new list with the strings filtered out.'''


def filter_list(l):
    final_list = []
    for element in l:
      if type(element)==int:
        final_list.append(element)
      else:
        pass
    return final_list

print(filter_list([1,'l', True, '2', 'b', 2]))