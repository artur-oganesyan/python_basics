def divide(dividend, divisor):
    """
    Quotient rounded to two decimal places
    """
    try:
        dividend = float(dividend)
        divisor = float(divisor)
        result = round(dividend / divisor, 2)
    except ZeroDivisionError:
        result = "Division by zero is impossible"
    except ValueError:
        result = "Variables should be a numbers"
    print("Quotient: ", result)


a = input("Enter dividend: ")
b = input("Enter divisor: ")
divide(a, b)
