import textwrap
import itertools

def sidebyside(left, right, width=79):
    length = 0
    if width % 2 == 0:
        length = int((width - 2) / 2)
    else:
        length = int((width - 1) / 2)
        
    wrapped_left = textwrap.wrap(left, length)
    wrapped_right = textwrap.wrap(right, length)
    
    zipped_list = list(itertools.zip_longest(wrapped_left, wrapped_right, fillvalue=" "))
    print(zipped_list)
    result = ''
    for item in zipped_list:
        result = result + item[0] + " " * (length - len(item[0])) + '|' + item[1] + " " * (length - len(item[1])) + '\n'
    
    return result
