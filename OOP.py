#class Fraction:
#    count = 0
#    def __init__(self, numerator = None, denominator = None):
#        self.numerator = numerator
#        self.denominator = denominator
#    
#    def set_fraction(self):
#        self.numerator = int(input('Введите числитель'))
#        self.denominator = int(input('Введите знаменатель'))
#    
#    def get_numerator(self):
#        print(f'Числитель: {self.numerator}')
#
#    def get_denominator(self):
#        print(f'Знаменатель: {self.denominator}')
#
#
#    def reduction(self, numerator, denominator):
#        for dlt in range(min(numerator, denominator), 0, -1):
#            if numerator % dlt == 0 and denominator % dlt == 0:
#                numerator = numerator // dlt
#                denominator = denominator // dlt
#        self.numerator = numerator
#        self.denominator = denominator
#
#    def summ(self):
#        other_numerator = int(input('Введите числитель второй дроби'))
#        other_denominator = int(input('Введите знаменатель второй дроби'))
#        summ_numerator = self.numerator * other_denominator + self.denominator * other_numerator
#        summ_denominator = self.denominator * other_denominator
#        self.reduction(summ_numerator, summ_denominator)
#    
#    def subtraction(self):
#        other_numerator = int(input('Введите числитель второй дроби'))
#        other_denominator = int(input('Введите знаменатель второй дроби'))
#        summ_numerator = self.numerator * other_denominator - self.denominator * other_numerator
#        summ_denominator = self.denominator * other_denominator
#        self.reduction(summ_numerator, summ_denominator)
#
#    def multiplication(self):
#        other_numerator = int(input('Введите числитель второй дроби'))
#        other_denominator = int(input('Введите знаменатель второй дроби'))
#        summ_numerator = self.numerator * other_numerator
#        summ_denominator = self.denominator * other_denominator
#        self.reduction(summ_numerator, summ_denominator)
#
#    def division(self):
#        other_numerator = int(input('Введите числитель второй дроби'))
#        other_denominator = int(input('Введите знаменатель второй дроби'))
#        summ_numerator = self.numerator * other_denominator
#        summ_denominator = self.denominator * other_numerator
#        self.reduction(summ_numerator, summ_denominator)
#
#
#
#first_fraction = Fraction(3, 4)
#print(first_fraction.__dict__)
#first_fraction.division()
#first_fraction.get_numerator()
#first_fraction.get_denominator()
#second_fraction = Fraction(33, 24)

#ИНКАПСУЛЯЦИЯ
# процедурный метод
#stack_list = []
#def add(stack, element):
#    stack.append(element)
#    return stack
#def delete(stack):
#    element = stack[-1]
#    stack.pop(-1)
#    return element
#add(stack_list, 1)
#add(stack_list, 2)
#print(add(stack_list, 3))
#print(delete(stack_list))
#stack_list[1] = 3567
#print(delete(stack_list))
#print(delete(stack_list))
# ООП
#class Stack:
#    def __init__(self):
#        self.stack_list = []
#    
#    def add(self, element):
#        self.stack_list.append(element)
#
#    def delete(self):
#        self.element = self.stack_list[-1]
#        self.stack_list.pop(-1)
#
#my_stack = Stack()
#my_stack.add(1)
#my_stack.add(2)
#my_stack.add(3)
#my_stack.stack_list[0] = 12
#print(my_stack.stack_list)
#my_stack.delete()
#print(my_stack.stack_list)
#my_stack.delete()
#print(my_stack.stack_list)
#my_stack.delete()

#НАСЛЕДОВАНИЕ
class MyClass:
    count = 0
    def __init__(self, name):
        self.name = name
        MyClass.count += 1
        self.id = MyClass.count

obj1 = MyClass('Первый')
obj2 = MyClass('Второй')
obj3 = MyClass('Третий')
print(MyClass.count, obj1.__dict__, obj2.id, obj3.id)

#ПОЛИМОРФИЗМ
#перегрузка метода с разным типом данных
#class Auto:
#    def __init__(self, manufacturer, model):
#        self.manufacturer = manufacturer
#        self.model = model
#    
#    def __str__(self):
#        return f'Auto {self.manufacturer}, model {self.model}'
#
#example_auto = Auto('Lada', 2107)
#example_auto2 = Auto('Tesla', 'E')
#print(example_auto)
#print(example_auto2)
#
# перегрузка с разным количеством параметров
#Условие: вводят длины сторон, нужно посчитать площадь фигуры. Иначе вывести сообщение об ошибке

class Figure:
    def __init__(self, *l): # (a = None, b = None, c = None, d = None)
        self.lenght = l

    def s(self):
        if len(self.lenght) == 3:
            p = round(sum(self.lenght) / 2, 2)
            a = self.lenght[0]
            b = self.lenght[1]
            c = self.lenght[2]
            self.square = (p * round(p - a,2) * round(p - b,2) * round(p - c,2)) ** 0.5
        elif len(self.lenght) == 4:
            a = list(set(self.lenght))[0]
            b = list(set(self.lenght))[1]
            self.square = a * b
        else:
            print('Некорректный ввод')


figure1 = Figure(25, 25, 49)
figure2 = Figure(3, 3, 5, 5)
figure1.s()
figure2.s()
print(figure1.square, figure2.square)