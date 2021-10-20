from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return self.param * 2 + 0.3

    def total_consumption(self, total_clothes):
        sum = 0
        for items in total_clothes:
            sum += items.consumption
        return sum


coat_1 = Coat(48)
coat_2 = Coat(56)
suit_1 = Suit(170)
suit_2 = Suit(195)
list_clothes = [coat_1, coat_2, suit_1, suit_2]

print(coat_1.consumption)
print(coat_2.consumption)
print(suit_1.consumption)
print(suit_2.consumption)
print(suit_1.total_consumption(list_clothes))
