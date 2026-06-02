import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name} мой уровень {self.level}')

    def attack(self):
        print(f'{self.name} наносит удар!')
        self.health -= 1

    def rest(self):
        print(f'{self.name} отдыхает…')
        self.health += 1

class Warrior (Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f'Воин {self.name} атакует мечом!')

class Mage (Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f'Маг {self.name} кастует заклинание!')


class Assassin (Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f'Ассасин {self.name} атакует из-под тишка!')


warrior = Warrior('Michael', 100, 1000, 5000, 10000)
mage = Mage("Marry", 111, 1111, 3000, 500)
assassin = Assassin("John", 130, 800, 7000, 8000)

hero_list = ["Warrior", "Mage", "Assassin"]

hero_wins_rule_dictionary = {
    "Warrior": "Assassin",
    "Assassin": "Mage",
    "Mage": "Warrior",
}


while True:
    selected_hero = input('Выберите героя: ').capitalize()
    if selected_hero in hero_list:
        break
    print('Неверный герой')

enemy = random.choice(hero_list)

if selected_hero == enemy:
    print("Ничья!")
elif hero_wins_rule_dictionary[selected_hero] == enemy:
    print(f"{selected_hero} победил!")
else:
    print(f"{enemy} победил!")