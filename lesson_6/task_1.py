import time


class TrafficLight:
    __red = "\U0001F534 \U000026AB \U000026AB"
    __yellow = "\U000026AB \U0001F7E1 \U000026AB"
    __green = "\U000026AB \U000026AB \U0001F7E2"

    def running(self):
        while True:
            self.light(self.__red, 7)
            self.light(self.__yellow, 2)
            self.light(self.__green, 7)
            self.light(self.__yellow, 2)

    def light(self, color, sec: int):
        for i in range(sec):
            print(f"\r{color}", f"{sec - i} sec.", end="")
            time.sleep(1)


t_light = TrafficLight()
t_light.running()
