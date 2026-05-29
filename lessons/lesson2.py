# Наследование
# Супер|Родительский класс
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} base action!!"

# subclass | дочерний класс
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp


    def action(self):
        return f"this new action {self.name}!!"

    def cast_spell(self):
        return f"{self.name} Fire!!"

kirito = Hero('kirito', 100, 1000)
gendalf_silver = MageHero('Gendalf', 100, -10000, 100)

print(gendalf_silver.hp)
print(gendalf_silver.cast_spell())
print(gendalf_silver.action())

# горизонтальное и ромбовидное наследование
# множественное наследование mro method resolution order

class Fly:
    def action(self):
        return "Fly"

class Swim:
    def action(self):
        return "Swim"

class Animal (Swim, Fly):
    ...
    # def action(self):
    #     return "action"

donald_duck = Animal()
print(donald_duck.action())

class A:
    def action(self):
        print("A")

class B(A):
    def action(self):
        super().action()
        print("B")

class C(A):
    def action(self):
        super().action()
        print("C")

class D(B, C):
    def action(self):
        super().action()
        print("D")

test_obj = D()

test_obj.action()
print(D.mro())