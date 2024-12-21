#Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def eat(self, food):
        print(f"{self.name} кушает {food}.")

# Пример использования
if __name__ == "__main__":
    # Создаем экземпляр Animal (нельзя, так как это абстрактный класс)
    # animal = Animal("Generic Animal", 5)  # Это вызовет ошибку

    # Создание подкласса
    class Dog(Animal):
        def make_sound(self):
            return "Гав"

    class Cat(Animal):
        def make_sound(self):
            return "Мяу"

    # Создаем экземпляры подклассов
    dog = Dog("Тай", 3)
    cat = Cat("Линкольн", 2)

    # Используем методы
    print(f"{dog.name} сказала: {dog.make_sound()}")
    dog.eat("мясные консервы")

    print(f"{cat.name} сказал: {cat.make_sound()}")
    cat.eat("корм феликс")