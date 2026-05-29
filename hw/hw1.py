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

kirito = Hero('kirito', 100, 1000, 5000)
asuna = Hero("Asuna", 111, 1111, 3000)

kirito.greet()
print(f'{kirito.name} health: {kirito.health}\n')

kirito.attack()
print(f'{kirito.name} health: {kirito.health}\n')

kirito.rest()
print(f'{kirito.name} health: {kirito.health}\n')

asuna.greet()
print(f'{asuna.name} health: {asuna.health}\n')

asuna.attack()
print(f'{asuna.name} health: {asuna.health}\n')

asuna.rest()
print(f'{asuna.name} health: {asuna.health}\n')

