class ZeroError(Exception):
    def __init__(self, text):
        self.text = text


class Cell:
    def __init__(self, size: int):
        try:
            if size > 0:
                self.size = size
            else:
                raise ZeroError("Cell size cannot be less than one")
        except ZeroError as e:
            print(e)

    def __add__(self, other):
        return Cell(self.size + other.size)

    def __sub__(self, other):
        return Cell(self.size - other.size)

    def __mul__(self, other):
        return Cell(self.size * other.size)

    def __truediv__(self, other):
        return Cell(self.size // other.size)

    def make_order(self, order):
        result = str()
        for row in range(self.size // order):
            result += "*" * order + "\n"
        result += "*" * (self.size % order)
        return result


cell_1 = Cell(3)
cell_2 = Cell(10)

add_cell = cell_1 + cell_2  # 30
sub_cell_1 = cell_1 - cell_2  #
sub_cell_2 = cell_2 - cell_1
mul_cell = cell_1 * cell_2
div_cell_1 = cell_1 / cell_2
div_cell_2 = cell_2 / cell_1

print()
print(add_cell.make_order(5))
print()
print(sub_cell_2.make_order(10))
print()
print(mul_cell.make_order(15))
print()
print(div_cell_2.make_order(1))
