def sum_array(num_list):
    if num_list is None:
        sum_value = 0
    elif len(num_list)>2:
        num_list.remove(max(num_list))
        num_list.remove(min(num_list))
        sum_value = sum(num_list)
    else:
        sum_value = 0
    return sum_value


