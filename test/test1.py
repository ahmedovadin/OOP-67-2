# наследование,
# инкапсуляция,
# переопределение методов,
# магические методы,
# абстрактные классы

class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f'{self.name} готов к бою!')

class MageHero (Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f'Маг {self.name} кастует заклинание! MP: {self.mp}')

class WarriorHero (Hero):
    def __init__(self, name, lvl, hp):
        super().__init__( name, lvl, hp)

    def action(self):
        print(f'Воин {self.name} рубит мечом! Уровень: {self.lvl}')

class BankAccount:
    bank_name = 'Asia Bank'
    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password):
        if password == self.__password:
            print('Пароль верный')
        else:
            print('Не верный пароль')

    def full_info(self):
        print(f'{self.hero.name} | Баланс: {self._balance} SOM')

    def get_bank_name(self):
        print(f'Банк: {self.bank_name}')

    def bonus_for_level(self):
        print(f'Бонус за уровень: {self.hero.lvl * 10} SOM')

    def __str__(self):
        print(f'{self.hero.name} Баланс: {self._balance} SOM')

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            print(f'Сумма счетов двух магов:: {self._balance + other._balance}')
        else:
            print('Нельзя сложить счета героев разных классов!')

    def __eq__(self, other):
        if type(self.hero) == type(other) and self.hero.lvl == other.lvl:
            print('Герои равные')

mage1 = MageHero('Merlin', 50, 100, 150)
mage2 = MageHero('Merlin', 1, 100, 150)
warrior = WarriorHero('Conan', 50, 100)
acc1 = BankAccount(mage1, 5000, '123321')
acc2 = BankAccount(mage2, 3000, '09877890')
acc3 = BankAccount(warrior, 1000, '1111')

mage1.action()
warrior.action()
acc1.full_info()
acc2.full_info()
acc1.get_bank_name()
acc1.bonus_for_level()
acc1.__add__(acc2)
acc1.__add__(acc3)

print(type(mage1) == type(mage2))
print(type(mage1) == type(warrior))





