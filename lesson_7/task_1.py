class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "".join(" ".join(map(str, row)) + "\n" for row in self.matrix)

    def __add__(self, other):
        result = list()
        for self_row, other_row in zip(self.matrix, other.matrix):
            new_row = list()
            for self_el, other_el in zip(self_row, other_row):
                new_row.append(self_el + other_el)
            result.append(new_row)
        return Matrix(result)


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(m_1 + m_2)
