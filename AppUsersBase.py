#■ Добавить нового пользователя +
#■ Удалить существующего пользователя +
#■ Проверить существует ли пользователь +
#■ Изменить логин существующего пользователя +
#■ Изменить пароль существующего пользователя
class User:
    def __init__(self, login, password, next_user=None):
        self.login = login
        self.password = password
        self.next_user = next_user

class UsersBase:
    head = None
    length = 0
    def __str__(self):
        line = f'Cписок пользователей:\n'
        current_user = self.head
        for i in range(self.length):
            line += f'Login: {current_user.login}, password: {current_user.password}\n'
            current_user = current_user.next_user
        return line

    def add_user(self, user):
        if self.head is None:
            self.head = user
        else:
            user.next_user = self.head
            self.head = user
        self.length += 1

    def search_of_login(self, login):
        current_user = self.head
        prev_user = None
        for index in range(self.length):
            if login == current_user.login:
                return current_user, prev_user
            else:
                prev_user = current_user
                current_user = current_user.next_user
        else:
            return None
    
    def delete_user(self, login):
        if login == self.head.login:
            current_user = self.head
            self.head = self.head.next_user
        else:
            current_user, prev_user = self.search_of_login(login)
            prev_user.next_user = current_user.next_user
        del current_user
        self.length -= 1

    def check_user(self, login):
        if self.search_of_login(login) is None:
            return False
        else:
            return True
    
    def update_login(self):
        login = input('Введите логин, который нужно заменить')
        current_user, prev_user = self.search_of_login(login)
        if current_user is None:
            print('Нет такого пользователя')
        else:
            new_login = input('Введите новый логин')
            current_user.login = new_login


array = UsersBase()
user1 = User('super_user', '123123')
user2 = User('admin', '1221')
user3 = User('mario', '333')
array.add_user(user1)
array.add_user(user2)
array.add_user(user3)
print(array.update_login())
print(array)

