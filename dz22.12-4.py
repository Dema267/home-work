class Animal():
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name} это {self.species}, возраст: {self.age}"


class Employee():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name}, должность: {self.position}"


class Zoo():
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal}")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен сотрудник: {employee}")

    def show_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(animal)

    def show_employees(self):
        print("Сотрудники в зоопарке:")
        for employee in self.employees:
            print(employee)


# Пример использования
if __name__ == "__main__":
    zoo = Zoo()

    # Добавляем животных
    lion = Animal("Симба", "Лев", 5)
    parrot = Animal("Констанция", "Попугай", 2)
    zoo.add_animal(lion)
    zoo.add_animal(parrot)

    # Добавляем сотрудников
    keeper = Employee("Михаил", "Администратор зоопарка")
    vet = Employee("Екатерина", "Ветеринар")
    zoo.add_employee(keeper)
    zoo.add_employee(vet)

    # Показываем животных и сотрудников
    zoo.show_animals()
    zoo.show_employees()