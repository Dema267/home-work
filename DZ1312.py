#система управления учетными записями пользователей для небольшой компании.
class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Защищенный атрибут
        self._name = name         # Защищенный атрибут
        self._access_level = 'user'  # Уровень доступа для обычных пользователей

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name, admin_level):
        super().__init__(user_id, name)  # Инициализация родительского класса
        self._access_level = 'admin'  # Уровень доступа для администраторов
        self._admin_level = admin_level  # Дополнительный уровень доступа администратора
        self._users = []  # Список пользователей

    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: Нужно передать объект User.")

    def remove_user(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                self._users.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Ошибка: Пользователь не найден.")

    def list_users(self):
        if not self._users:
            print("Нет пользователей в системе.")
        else:
            print("Список пользователей:")
            for user in self._users:
                print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")


# Пример использования
if __name__ == "__main__":
    admin = Admin(user_id=1, name="Администратор", admin_level="super")
    user1 = User(user_id=2, name="Сотрудник 1")
    user2 = User(user_id=3, name="Сотрудник 2")

    admin.add_user(user1)
    admin.add_user(user2)

    admin.list_users()

    admin.remove_user(2)
    admin.list_users()