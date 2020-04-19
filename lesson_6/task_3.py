class Worker:
    def __init__(self, name, surname, position, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


p = Position("John", "Johnson", "Designer", 2000, 750)
print(p.get_full_name())
print(p.get_total_income())
