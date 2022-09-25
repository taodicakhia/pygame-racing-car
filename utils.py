def edit_tuple(tuple_list, index, new_element):
    x = list(tuple_list)
    x[index] = new_element
    return tuple(x)