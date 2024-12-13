class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина."""
        self.items[item_name] = price
        print(f'Товар "{item_name}" добавлен с ценой {price}.')

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]
            print(f'Товар "{item_name}" удален из ассортимента.')
        else:
            print(f'Товар "{item_name}" не найден в ассортименте.')

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f'Цена товара "{item_name}" обновлена на {new_price}.')
        else:
            print(f'Товар "{item_name}" не найден в ассортименте.')

# Создание объектов класса Store
store1 = Store("Табрис", "Улица Ленина, 7а")
store1.add_item("яблоки голден", 135)
store1.add_item("бананы", 150)
store1.add_item( ("бананы", 150)

store2 = Store("Табрис-2", "Проспект Мира, 44")
store2.add_item("молоко", 97)
store2.add_item("кефир", 85)

store3 = Store("Табрис-3", "Улица Астраханская, 108")
store3.add_item("курица", 220)
store3.add_item("свинина", 310)

# Тестирование методов на одном из магазинов
print("\nТестирование методов на магазине 'Табрис':")
store1.add_item("мандарины Абхазия", 115)  # Добавление товара
print(f'Цена на яблоки: {store1.get_price("яблоки голден")}')  # Получение цены
store1.update_price("бананы", 135)  # Обновление цены
print(f'Обновленная цена на бананы: {store1.get_price("бананы")}')
store1.remove_item("яблоки голден")  # Удаление товара
print(f'Цена на яблоки после удаления: {store1.get_price("яблоки голден")}')