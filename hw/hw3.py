from abc import ABC, abstractmethod
from ctypes import wstring_at


class Hero(ABC):
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.__health = health

    def greet(self):
        print(f'Привет, я {self.name} мой уровень {self.level}')

    def rest(self):
        print(f'{self.name} отдыхает')
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass

class Warrior (Hero):
    def __init__(self, name, level, health, stamina):
        super().__init__(name, level, health )
        self.stamina = stamina

    def attack(self):
        print(f'Воин {self.name} атакует мечом!')

class Mage (Hero):
    def __init__(self, name, level, health, mana):
        super().__init__(name, level, health)
        self.mana = mana
    def attack(self):
        print(f'Маг {self.name} использует магию')

class Assassin (Hero):
    def __init__(self, name, level, health, stealth):
        super().__init__(name, level, health)
        self.stealth = stealth

    def attack(self):
        print(f'Ассасин {self.name} атакует из-под тишка')

warrior = Warrior('Michael', 100, 1000, 10000)
mage = Mage("Marry", 111, 1111, 500)
assassin = Assassin("John", 130, 800, 8000)

warrior.greet()
warrior.attack()
warrior.rest()

mage.greet()
mage.attack()
mage.rest()

assassin.greet()
assassin.attack()
assassin.rest()
