class Complex:
    def __init__(self, number):
        self.complex = complex(number)

    def __add__(self, other):
        return self.complex + other.complex

    def __mul__(self, other):
        return self.complex * other.complex


c_1 = Complex(5)
c_2 = Complex(7)

print(c_1 + c_2)
print(c_1 * c_2)
