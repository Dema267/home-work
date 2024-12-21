#Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def eat(self, food):
        print(f"{self.name} кушает {food}.")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span  # Специфический атрибут для птиц

    def make_sound(self):
        return "Чик-чирик!"

    def fly(self):
        print(f"{self.name} летит с размахом крульев {self.wing_span} метров.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color  # Специфический атрибут для млекопитающих

    def make_sound(self):
        return "рычание"

    def groom(self):
        print(f"{self.name} ухаживает за своей {self.fur_color} шерстью.")

class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color  # Специфический атрибут для рептилий

    def make_sound(self):
        return "шипит"

    def bask(self):
        print(f"{self.name} греется на солнце.")

# Пример использования
if __name__ == "__main__":
    parrot = Bird("Поли", 2, 0.5)
    lion = Mammal("Симба", 5, "песочной")
    snake = Reptile("Слизерен", 3, "черная")

    # Используем методы
    print(f"{parrot.name} сказал: {parrot.make_sound()}")
    parrot.eat("семена")
    parrot.fly()

    print(f"{lion.name} сказал: {lion.make_sound()}")
    lion.eat("антилопу")
    lion.groom()

    print(f"{snake.name} сказала: {snake.make_sound()}")
    snake.eat("Гарри Поттера")
    snake.bask()
