# def test():
#     print("test")
#
# test()

class Hero:
    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты объекта класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    # Метод класса
    def rest(self):
        return  f"{self.name} Отдыхает на чиле на расслабоне!!"

# Объект|Экземпляр на основе класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 111, 1111)
print(kirito.rest())
print(asuna.rest())
my_str_1 = "hgfds"
my_str_2 = "hgfds"
print(my_str_1.capitalize())
print(my_str_2.capitalize())

# MageHero
# hero_kirito
