# динамический массив
#array = [43, 534, 54,576, 7, 786, 32]
#print(array[3])
#array.append(-1) # предпочтителен по скорости
#array.insert(3, 0)
#array.remove(7)
#array.pop(2)
#print(array)
#

#Задание 1
#Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо 
#сохранить в односвязный
#список. После чего нужно показать меню, в котором
#предложить пользователю набор пунктов:
#1. Добавить элемент в список.+
#2. Удалить элемент из списка.+
#3. Показать содержимое списка.+
#4. Проверить есть ли значение в списке.+
#5. Заменить значение в списке.+
#В зависимости от выбора пользователя выполняется
#действие, после чего меню отображается снова.

class LinkList:
    lenght = 0
    head = None
    class Node:
        def __init__(self, value, next_node = None):
            self.value = value
            self.next_node = next_node

    def my_append(self, value):
        if self.head is None:
            self.head = LinkList.Node(value) 
        else:
            current_node = self.head
            while current_node.next_node != None:
                current_node = current_node.next_node
            current_node.next_node =  LinkList.Node(value)
        self.lenght += 1

    def __str__(self):
        result_line = '<$'
        current_node = self.head
        while current_node.next_node != None:
            result_line += f'{current_node.value}, '
            current_node = current_node.next_node
        result_line += f'{current_node.value}$>'
        return result_line
    
    def search(self, value_from_search):
        current_node = self.head
        while current_node.next_node != None:
            if current_node.value == value_from_search:
                return True
            current_node = current_node.next_node
        if current_node.value == value_from_search:
            return True
        else:
            return False

    def my_remove(self, value_from_remove):
        current_node = self.head
        if current_node.value == value_from_remove:
            self.head = current_node.next_node
            del current_node
            self.lenght -= 1
            return 'Элемент удален'
        while current_node.next_node != None:
            print(current_node.value)
            if current_node.next_node.value == value_from_remove:
                current_next_node = current_node.next_node.next_node
                del current_node.next_node
                current_node.next_node = current_next_node
                self.lenght -= 1
                return 'Элемент удален'
            current_node = current_node.next_node
        return 'Элемент для удаления не найден'

    def update(self, old_value, new_value):
        current_node = self.head
        while current_node.next_node != None:
            if current_node.value == old_value:
                current_node.value = new_value
                return 'Данные обновлены'
            current_node = current_node.next_node
        if current_node.value == old_value:
            current_node.value = new_value
            return 'Данные обновлены'
        else:
            return 'Данные не обновлены'

my_array = LinkList()
my_array.my_append(52)
my_array.my_append(-5)
my_array.my_append(0)
my_array.my_append(5342)
my_array.my_remove(0)
print(my_array)
#print(my_array)


#array = input('Введите числа через пробел.')
#link_list = LinkList()
#array = array.split(' ')
#for elem in array:
#    link_list.my_append(elem)
#
#while True:
#    print(f'Ваш массив чисел: {link_list}')
#    choice = input(f'1-добавить\n2-удалить\n3-поиск\n4-заменить\n5-вывод\n0-выход')
#    if choice == '1':
#        value = input('Введите значение для добавления')
#        link_list.my_append(value)
#    elif choice == '2':
#        value = input('Введите значение для удаления')
#        link_list.my_remove(value)
#    elif choice == '3':
#        value = input('Введите значение для поиска')
#        print(link_list.search(value))
#    elif choice == '4':
#        old_value = input('Введите заменяемое значение')
#        new_value = input('Введите заменяющее значение')
#        link_list.update(old_value, new_value)
#    elif choice == '0':
#        break
#print('Программа завершена')
    