class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span  # Специфический атрибут для птиц

    def make_sound(self):
        return "Chirp!"

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wing_span} meters.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color  # Специфический атрибут для млекопитающих

    def make_sound(self):
        return "Roar!"

    def groom(self):
        print(f"{self.name} is grooming its {self.fur_color} fur.")

class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color  # Специфический атрибут для рептилий

    def make_sound(self):
        return "Hiss!"

    def bask(self):
        print(f"{self.name} is basking in the sun.")

# Пример использования
if __name__ == "__main__":
    parrot = Bird("Polly", 2, 0.5)
    lion = Mammal("Leo", 5, "golden")
    snake = Reptile("Slither", 3, "green")

    # Используем методы
    print(f"{parrot.name} says: {parrot.make_sound()}")
    parrot.eat("seeds")
    parrot.fly()

    print(f"{lion.name} says: {lion.make_sound()}")
    lion.eat("meat")
    lion.groom()

    print(f"{snake.name} says: {snake.make_sound()}")
    snake.eat("mouse")
    snake.bask()