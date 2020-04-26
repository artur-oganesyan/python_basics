class MyErrorZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


def divide(dividend, divisor):
    """
    Quotient rounded to two decimal places
    """
    try:
        dividend = float(dividend)
        divisor = float(divisor)
        if divisor == 0:
            raise MyErrorZeroDivision("Division by zero is impossible")
        result = round(dividend / divisor, 2)
    except MyErrorZeroDivision as err:
        result = err
    except ValueError:
        result = "Variables should be a numbers"
    print("Quotient:", result)


a = input("Enter dividend: ")
b = input("Enter divisor: ")
divide(a, b)