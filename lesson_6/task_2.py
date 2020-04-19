class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self, weight_per_square, thickness):
        return f"{round((self._length * self._width * weight_per_square * thickness) / 1000)} t."


r = Road(5000, 20)
print(r.calc_weight(25, 5))
