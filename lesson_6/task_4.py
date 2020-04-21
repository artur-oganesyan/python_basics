class Car:
    def __init__(self, speed: int, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Car name: {self.name}, color: {self.color},"
              f" speed: {self.speed}, police car: {self.is_police}")

    def go(self):
        print(f"Car {self.name} started.")

    def stop(self):
        print(f"Car {self.name} stopped.")

    def turn(self, direction):
        print(f"Car {self.name} goes {direction}.")

    def show_speed(self):
        print(f"Speed of car {self.name} {self.speed} km/h.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("You exceeded the speed limit. ", end="")
        super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("You exceeded the speed limit. ", end="")
        super().show_speed()


class PoliceCar(Car):
    pass


town_car = TownCar(60, "black", "Volkswagen", False)
town_car.go()
town_car.show_speed()
town_car.turn("left")
town_car.stop()
print()

sport_car = SportCar(110, "red", "Lexus", False)
sport_car.go()
sport_car.show_speed()
sport_car.turn("forward")
sport_car.stop()
print()

work_car = WorkCar(45, "white", "Mazda", False)
work_car.go()
work_car.show_speed()
work_car.turn("right")
work_car.stop()
print()

police_car = PoliceCar(90, "blue", "Ford", True)
police_car.go()
police_car.show_speed()
police_car.turn("back")
police_car.stop()
