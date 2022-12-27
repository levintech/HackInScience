def flatten(a_list):

    flatten_list = []    
    for item in a_list:
        print(item)
        if type(item) == list:
            flatten_list = flatten_list + flatten(item)
        else:
            flatten_list.append(item)
    
    return flatten_list