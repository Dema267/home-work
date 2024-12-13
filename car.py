class Car:
    def __init__(self, make, model):
        self.public_make = make # Открытый атрибут
        self ._protected_model = model # Защищенный атрибут
        self .__private_year = 2022 # Приватный атрибут

    def public_method(self):
        return f"Это открытый метод. Машина: {self.public_make} {self._protected_model}."

    def protected_method(self):
        return "Это защищенный метод."

    def private_method(self):
        return "Это приватный метод."



class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super(). __init__(make, model)  # Вызов конструктора родительского класса
        self.battery_size = battery_size  # Инициализация размера батареи



    def get_details(self):
        # Можно обратиться к открытому и защиценному атрибуту, но не к приватному
        details = f"{self.public_make} {self ._protected_model}, 5atapes: {self.battery_size} kWh."
        # Нельзя напряную обратиться к __private_method и __ private_year
        return details

tesla = ElectricCar("Tesla", "Model S", 100)

print(tesla.public_make)
print(tesla.public_method())

print(tesla._Car__private_year)

