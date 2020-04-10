def my_func(x, y):
    """
    Raising a positive number to a negative power
    :param x: a real positive number
    :param y: a negative integer
    """
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        return "Error. Variable 'X' should be a real positive number. Variable 'Y' should be a negative integer"
    if x < 0:
        return "Variable 'X' should be a real positive number"
    elif y > 0:
        return "Variable 'Y' should be a negative integer"
    else:
        # solution 1
        result = 1
        for i in range(abs(y)):
            result *= x
        return 1 / result
        # solution 2
        # return x ** y


print(my_func(1, -1))
