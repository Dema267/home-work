class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_info(self):
        return f"Имя: {self.name}, сотрудник ID: {self.employee_id}"


class ZooKeeper(Employee):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)

    def feed_animal(self, animal_name):
        return f"{self.name} кормит {animal_name}."


class Veterinarian(Employee):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)

    def heal_animal(self, animal_name):
        return f"{self.name} лечит {animal_name}."


# Пример использования классов
if __name__ == "__main__":
    zookeeper = ZooKeeper("Екатерина", 1)
    veterinarian = Veterinarian("Андрей", 2)

    print(zookeeper.get_info())
    print(zookeeper.feed_animal("Льва"))

    print(veterinarian.get_info())
    print(veterinarian.heal_animal("Жирафа"))