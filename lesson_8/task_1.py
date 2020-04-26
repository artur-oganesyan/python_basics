class Date:
    def __init__(self, date: str):
        self.date = date
        day, month, year = Date.parse_date(date)
        Date.validate_date(day, month, year)

    @classmethod
    def parse_date(cls, date: str):
        day, month, year = date.split("-")
        return int(day), int(month), int(year)

    @staticmethod
    def validate_date(day, month, year):
        if 1 <= month <= 12:
            print("Month is valid")
        else:
            print("Month should be from 1 to 12")
        if 1 <= day <= 31:
            print("Day is valid")
        else:
            print("Day should be from 1 to 31")
        if year > 0:
            print("Year is valid")

        else:
            print("Year should be positive number")


d = Date("10-10-2020")
