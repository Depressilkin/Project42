#Задание 2
#Пользователь вводит с клавиатуры набор строк. Полученные строки необходимо сохранить в двусвязный
#список. После чего нужно показать меню, в котором
#предложить пользователю набор пунктов:
#1. Добавить элемент в список +
#2. Удалить элемент из списка 
#3. Показать содержимое списка +
#4. Проверить есть ли значение в списке +
#5. Заменить значение в списке
#В зависимости от выбора пользователя выполняется
#действие, после чего меню отображается снова. 
class Node:
    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class DoubleLinkList:
    head = None
    tail = None
    length = 0
    #методы
    def my_append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            #current_node = self.head
            #while current_node.next_node != None:
            #    current_node = current_node.next_node
            #current_node.next_node = Node(value, prev_node = current_node)
            #self.tail = current_node.next_node
            current_node = self.tail
            current_node.next_node = Node(value, prev_node = current_node)
            self.tail = current_node.next_node
        self.length += 1

    def __str__(self):
        line = '<<'
        current_node = self.head
        while current_node.next_node != None:
            line += f'{current_node.value}; '
            current_node = current_node.next_node
        line += f'{current_node.value}>>'
        return line
    
    def get_value(self, value_from_search):
        current_node = self.head
        while current_node.next_node != None:
            if current_node.value == value_from_search:
                return True
            current_node = current_node.next_node
        if current_node.value == value_from_search:
                return True
        else:
            return False
            
    def del_value(self,value_from_delete):
        if self.head.value == value_from_delete:# если удаляется голова
            node_from_delete = self.head
            self.head = self.head.next_node
            self.head.prev_node = None
            
        elif self.tail.value == value_from_delete:# если удаляется хвост
            node_from_delete = self.tail
            self.tail = self.tail.prev_node
            self.tail.next_node = None
           
        else:
            current_node = self.head # если удаляется что-то между головой и хвостом
            while current_node.next_node != None:
                if current_node.value == value_from_delete:
                    node_from_delete = current_node
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                current_node = current_node.next_node
        del node_from_delete
        self.length -= 1

    def update_value(self,old_value, value_from_update):
        current_node = self.head 
        while current_node.next_node != None:
            if current_node.value == old_value:
                current_node.value = value_from_update
            current_node = current_node.next_node
        if current_node.value == old_value:
            current_node.value = value_from_update
        

#Задание 3
#Реализуйте класс стека для работы с целыми значениями (стек целых).
#Стек должен иметь фиксированный размер.
#Реализуйте набор операций для работы со стеком:
#■ помещение целого значения в стек;+
#■ выталкивание целого значения из стека;+
#■ подсчет количества целых в стеке;+
#■ проверку пустой ли стек;+
#■ проверку полный ли стек;+
#■ очистку стека;+
#■ получение значения без выталкивания верхнего целого в стеке.
#При старте приложения нужно отобразить меню с
#помощью, которого пользователь может выбрать необходимую операцию
class Stack:
    head = None
    tail = None
    length = 0
    max_length = 5

    def stack_append(self, value):
        if self.length < self.max_length:
            if self.head == None:
                self.head = Node(value)
                self.tail = self.head
            else:
                current_node = self.tail
                current_node.next_node = Node(value, prev_node = current_node)
                self.tail = current_node.next_node
            self.length += 1
        else:
            print('Стэк заполнен')
    
    def stack_pop(self):  
        node_from_delete = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None 
        self.length -= 1
        del node_from_delete

    def get_length(self):
        print(f'Элементов в стэке: {self.length}')

    def check_empty(self):
        if self.head is None:
            print('Стэк пуст')
        else:
            print('Стэк не пуст')
    
    def stack_clear(self):
        current_node = self.head
        while current_node.next_node != None:
            node_from_delete = current_node
            current_node = current_node.next_node
            del node_from_delete
        del current_node
        self.length = 0
        self.head = None
        self.tail = None

    def get_tail(self):
        print(f'Последний элемент: {self.tail.value}')



my_stack = Stack()
array = input('Введите числа через пробел, максимальное количество пять шт.')

array = array.split(' ')
for elem in array:
    my_stack.stack_append(elem)

while True:
    choice = input(f'1-добавить\n2-удалить\n3-вывод последнего\n4-проверка пустоты\n5-очистить\n0-выход')
    if choice == '1':
        value = input('Введите значение для добавления')
        my_stack.stack_append(value)
    elif choice == '2':
        my_stack.stack_pop()
    elif choice == '3':
        my_stack.get_tail()
    elif choice == '4':
        my_stack.check_empty()
    elif choice == '5':
        my_stack.stack_clear()
    elif choice == '0':
        break
print('Программа завершена')




        

