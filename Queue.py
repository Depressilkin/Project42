#Создайте класс очереди для работы с символьными
#значениями. Требуется создать реализации для операций
#над элементами:
#■ IsEmpty —роверка очереди на пустоту.+
#■ IsFull — проверка очереди на заполнение.
#■ Enqueue — добавление элемента в очередь.+
#■ Dequeue — удаление элемента из очереди.+
#■ Show — отображение всех элементов очереди на +
#экран.
#При старте приложения нужно отобразить меню
#-
#обходимую операцию

#class Node:
#    def __init__(self, name, next_node = None, prev_node = None):
#        self.name = name
#        self.next_node = next_node
#        self.prev_node = prev_node
#
#class Queue:
#    length = 0
#    max_length = 8
#    head = None
#    tail = None
#    def enqueue(self, name):
#        if self.head is None:
#            self.head = self.tail = Node(name)
#            self.length += 1
#        elif self.length < self.max_length:
#            new_node = Node(name, prev_node = self.tail)
#            self.tail.next_node = new_node
#            self.tail = new_node
#            self.length += 1
#        else:
#            print(f'Очередь заполнена')
#    
#    def show(self):
#        try:
#            num_in_queue = 1
#            line = f'Очередь: '
#            current_node = self.head
#            while current_node.next_node != None:
#                line += f'{num_in_queue} - {current_node.name}, '
#                num_in_queue += 1
#                current_node = current_node.next_node
#            line += f'{num_in_queue} - {current_node.name}.'
#            return line
#        except:
#            return f'Очередь пуста'
#
#    def dequeue(self):
#        try:
#            if self.head.next_node is None:
#                del self.head
#            else:
#                self.head = self.head.next_node 
#                del self.head.prev_node
#            self.length -= 1
#        except:
#            print('Удалять некого! Очередь Пуста.')
#    
#    def is_empty(self):
#        if self.length == 0:
#            print('Очередь пуста.')
#            return True
#        else:
#            print('Очередь не пуста!')
#            return False
#
#    def is_full(self):
#        if self.length == self.max_length:
#            print('Очередь заполнена.')
#            return True
#        else:
#            print('Очередь не заполнена!')
#            return False
#queue_in_market = Queue()
#queue_in_market.enqueue('Ivan')
#queue_in_market.enqueue('Ivan2')
#queue_in_market.enqueue('Ivan3')
#queue_in_market.enqueue('Ivan4')
#queue_in_market.enqueue('Ivan5')
#queue_in_market.enqueue('Ivan3')
#queue_in_market.enqueue('Ivan4')
#queue_in_market.enqueue('Ivan5')
#queue_in_market.is_full()
#queue_in_market.dequeue()
#queue_in_market.dequeue()
#queue_in_market.is_full()
#
#print(queue_in_market.show())

#Создайте класс очереди с приоритетами для работы
#с символьными значениями.
#Требуется создать реализации для операций над элементами очереди:
#■ IsEmpty — проверка очереди на пустоту.
#■ IsFull — проверка очереди на заполнение.
#  PullHighestPriorityElementудаление элемента с самым высоким приоритетом из очереди.+
#■ InsertWithPriority — добавление элемента c приоритетом в очередь.+
#мым высоким приоритетом из очереди.
#■ Peek — возврат самого большого по приоритету элемента. Обращаем ваше внимание, что элемент не
#удаляется из очереди.
#■ Show — отображение всех элементов очереди на экран. +
class Node:
    def __init__(self, task, priority, next_node = None, prev_node = None):
        self.task = task
        self.priority = abs(float(priority))
        self.next_node = next_node
        self.prev_node = prev_node
        
class PriorityQueue:
    head = None
    length = 0
    max_lenght = 5

    def show(self):
        if self.head is None:
            print('Очередь пуста')
        else:
            line = f'Очередь: \n'
            current_node = self.head
            while current_node.next_node != None:
                line += f'#{current_node.priority}# {current_node.task};'
                current_node = current_node.next_node
            line += f'#{current_node.priority}# {current_node.task}.'
            print(line)
            return line


    def insert_with_priority(self, task, priority):
        #new_node = Node()
        if self.head is None:
            self.head = Node(task, priority)
            self.length += 1
        elif self.length < self.max_lenght:
            current_node = self.head
            if priority < current_node.priority:
                current_node.prev_node = Node(task, priority, next_node=current_node)
                self.head = current_node.prev_node
                self.length += 1
                return f'элемент добавлен'
            while current_node.next_node != None:
                if current_node.priority > priority:
                    #current_node.prev_node.next_node = Node(task, priority, next_node=current_node, prev_node=current_node.prev_node)
                    #current_node.prev_node = current_node.prev_node.next_node
                    new_node = Node(task, priority, next_node=current_node, prev_node=current_node.prev_node)
                    current_node.prev_node.next_node = new_node
                    current_node.prev_node = new_node
                    self.length += 1
                    return f'элемент добавлен'
                else:
                    current_node = current_node.next_node
            if priority < current_node.priority:
                current_node.prev_node.next_node = current_node.prev_node =  Node(task, priority, next_node=current_node, prev_node = current_node.prev_node)
            else:
                current_node.next_node = Node(task, priority, prev_node=current_node) 
            self.length += 1
            return f'элемент добавлен'
        else:
            return f'Добавление невозможно! Очередь заполнена'

    def pull_highest_priority_element(self):
        try:
            if self.length > 1:
                self.head = self.head.next_node
                del self.head.prev_node
            else:
                del self.head
            self.length -= 1
        except:
            print('Очередь пуста')

    def peek(self):
        if self.length != 0:
            print(f'#{self.head.priority}# {self.head.task}.')
            return f'#{self.head.priority}# {self.head.task}.'
        else:
            print('Очередь пуста')

todo = PriorityQueue()
todo.insert_with_priority('задание 1', 2)
todo.insert_with_priority('задание 2', -1)
todo.insert_with_priority('задание 4', 0.7)
todo.insert_with_priority('задание 5', 0.9)
todo.insert_with_priority('задание 5', 3)
todo.pull_highest_priority_element()
todo.pull_highest_priority_element()
todo.peek()
#todo.show()



