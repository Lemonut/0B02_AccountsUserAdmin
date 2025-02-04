class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Защищенный атрибут
        self.__name = name  # Приватный атрибут
        self.access_level = "user"  # Уровень доступа для обычных пользователей

    # Метод для получения приватного имени
    def get_name(self):
        return self.__name

    # Метод для установки приватного имени
    def set_name(self, name):
        self.__name = name

    # Метод для получения ID
    def get_id(self):
        return self._user_id


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.access_level = 'admin'  # Уровень доступа для администраторов
        self.user_list = []  # Список пользователей

    def add_user(self, user):
        try:
            # Проверяем, можем ли мы вызвать метод get_name
            user.get_name()
            self.user_list.append(user)
            print(f"User {user.get_name()} is added to the list.")
        except AttributeError:
            print("Only User instances can be added.")

    # Метод для удаления пользователя
    def remove_user(self, user):
        if user in self.user_list:
            self.user_list.remove(user)
            print(f"User {user.get_name()} is removed from the list.")
        else:
            print("User not found in the list.")


# Примеры использования
user1 = User("34", "John")
admin1 = Admin("55", "Mari")

# Проверка доступа
print(f"{user1.get_name()} has {user1.access_level} access")
print(f"{admin1.get_name()} has {admin1.access_level} access")

# Добавление и удаление пользователей
admin1.add_user(user1)  # Добавляем обычного пользователя
admin1.remove_user(user1)  # Удаляем пользователя


