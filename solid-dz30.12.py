#Разработать простую игру с приминением принципа SOLID, где игрок может использовать различные типы оружия для борьбы с монстрами.
from abc import ABC, abstractmethod

# Шаг 1: Создаем абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage
        return self.health <= 0

# Шаг 3: Модифицируем класс Fighter
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack_monster(self, monster: Monster):
        print(self.weapon.attack())
        if monster.take_damage(100):
            print(f"{monster.name} побежден!")

# Шаг 4: Реализация боя
if __name__ == "__main__":
    # Создаем бойца и монстра
    fighter = Fighter("Герой", Sword())
    monster = Monster("Дракон")

    # Бой с мечом
    fighter.attack_monster(monster)

    # Меняем оружие на лук
    fighter.change_weapon(Bow())

    # Бой с луком
    fighter.attack_monster(monster)