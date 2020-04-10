def my_func(var_1, var_2, var_3):
    """
    Variables should be a naturals numbers.

    :return: sum of the two largest values
    """
    try:
        my_list = [int(var_1), int(var_2), int(var_3)]
        my_list.remove(min(my_list))
        return sum(my_list)
    except ValueError:
        return "Variables should be a naturals numbers"


print(my_func(4, 6, 3))
