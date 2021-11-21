def merge_lists(set_1:list, set_2:list) ->list:
    new_list = list(set(set_1+set_2))
    new_list = [element**3 for element in new_list]
    return new_list


set_1 = [2,3,4,6]
set_2 = [5,6,7,4]

merge_lists(set_1, set_2)