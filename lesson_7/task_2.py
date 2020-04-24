from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def cloth_count(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def cloth_count(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, length):
        self.length = length

    @property
    def cloth_count(self):
        return round(2 * self.length + 0.3, 2)


coat = Coat(50)
suit = Suit(180)
print(coat.cloth_count)
print(suit.cloth_count)
print(coat.cloth_count + suit.cloth_count)
