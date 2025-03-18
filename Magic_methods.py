##MAГИЧЕСКИЕ МЕТОДЫ
#class MyClass:
#    # ПРИ ВЫЗОВЕ КОНСТРУКТОРА __init__()
#    def __init__(self, name, value):
#        self.name = name
#        self.value = value
#    # при выводе в print метод __str__
#    def __str__(self):
#        return f'Меня зовут {self.name}'
#    # при сравнении
#    #__lt__(self, other) — определяет поведение оператора сравнения «меньше», <.
##
#    #__le__(self, other) — определяет поведение оператора сравнения «меньше или равно», <=.
##
#    #__eq__(self, other) — определяет поведение оператора «равенства», ==.
##
#    #__ne__(self, other) — определяет поведение оператора «неравенства», !=.
##
#    #__gt__(self, other) — определяет поведение оператора сравнения «больше», >.
##
#    #__ge__(self, other) — определяет поведение оператора сравнения «больше или равно», >=.
#    def __eq__(self, other):
#        if isinstance(other, MyClass):
#            if self.value == other.value:
#                return f'Равные значения'
#            else:
#                return f'Неравные'
#        else:
#            return f'Это экземпляр другого класса'
#
#    # математические операторы
##   __add__(self, other) — сложение, оператор +
#
##   __sub__(self, other) — вычитание, оператор -
##   
##   __mul__(self, other) — умножение, оператор *
##   
##   __truediv__(self, other) — деление, оператор /
##   
##   __pow__(self, other[, modulo]) — возведение в степень, оператор **
#    def __add__(self, other):
#       if isinstance(other, MyClass):
#           return self.value + other.value
#       else:
#            return f'Это экземпляр другого класса'
#    def __pow__(self, other):
#        if isinstance(other, MyClass):
#           return self.value ** other.value
#        else:
#            return f'Это экземпляр другого класса'
#
#class SecondClass:
#    pass
#
#obj = MyClass('Мой Класс', 10)
#obj2 = MyClass('второй класс', -1)
#ob = SecondClass()
#sum = obj + 6
#print(obj.value ** obj2.value)


#Создайте класс Число (или используйте уже ранее
#созданный вами). Класс число хранит внутри одно значение. Используя перегрузку операторов реализуйте для
#него арифметические операции для работы с числом
#(операции +, -, *, /).

#class Number:
#    def __init__(self, value):
#        self.value = value
#    
#    def __sub__(self, other):
#        if isinstance(other, Number):
#            return self.value - other.value
#        else:
#            return f'Это экземпляр другого класса'
#        
#    def __add__(self, other):
#        if isinstance(other, Number):
#            return self.value + other.value
#        else:
#            return f'Это экземпляр другого класса'
#        
#    def __mul__(self, other):
#        if isinstance(other, Number):
#            return self.value * other.value
#        else:
#            return f'Это экземпляр другого класса'
#    
#    def __truediv__(self, other):
#        if isinstance(other, Number):
#            return self.value / other.value
#        else:
#            return f'Это экземпляр другого класса'
#
#numb1 = Number(5)
#numb2 = Number(3)
#sub = numb2 - numb1
#summ = numb2 + numb1
#mult = numb2 * numb1
#divis = numb2 / numb1
#print(sub, summ, mult, divis)

#Создайте класс Дробь (или используйте уже ранее
#созданный вами). Используя перегрузку операторов реализуйте для него арифметические операции для работы
#с дробями (операции +, -, *, /).

#class Fraction:
#    
#    def __init__(self, numerator = None, denominator = None):
#        self.numerator = numerator
#        self.denominator = denominator
#    @staticmethod
#    def reduction(numerator, denominator):
#        for dlt in range(min(numerator, denominator), 0, -1):
#            if numerator % dlt == 0 and denominator % dlt == 0:
#                numerator = numerator // dlt
#                denominator = denominator // dlt
#        return numerator, denominator
#
#    def __add__(self, other):
#        summ_numerator = self.numerator * other.denominator + self.denominator * other.numerator
#        summ_denominator = self.denominator * other.denominator
#        result =  Fraction.reduction(summ_numerator, summ_denominator)
#        return f'Результат суммы: {result[0]}/{result[1]}'
#    
#    def __sub__(self, other):
#        summ_numerator = self.numerator * other.denominator - self.denominator * other.numerator
#        summ_denominator = self.denominator * other.denominator
#        result =  Fraction.reduction(summ_numerator, summ_denominator)
#        return f'Результат разности: {result[0]}/{result[1]}'
#
#    def __mul__(self, other):
#        summ_numerator = self.numerator * other.numerator
#        summ_denominator = self.denominator * other.denominator
#        result =  Fraction.reduction(summ_numerator, summ_denominator)
#        return f'Результат произведения: {result[0]}/{result[1]}'
#
#    def __truediv__(self, other):
#        summ_numerator = self.numerator * other.denominator
#        summ_denominator = self.denominator * other.numerator
#        result =  Fraction.reduction(summ_numerator, summ_denominator)
#        return f'Результат деления: {result[0]}/{result[1]}'
#
#frac1 = Fraction(3,4)
#frac2 = Fraction(2,6)
#summ = frac1 + frac2
#sub = frac1 - frac2
#mult = frac1 * frac2
#divis = frac1 / frac2
#print(summ, sub, mult, divis)
#

#Создайте класс Библиотека. Класс предназначен для
#хранения информации о библиотеке (название, адрес, количество книг и т.д.). Реализуйте необходимые для класса
#методы. Используя перегрузку операторов реализуйте для
#него следующие арифметические операции:
#■ + добавляет к количеству книг указанное значение;
#■ - вычитает из количества книг указанное значение;
#■ += добавляет к количеству книг указанное значение;
#■ -= вычитает из количества книг указанное значение;
#Используя перегрузку операторов реализуйте (сравнение по количеству книг):
#■ <;
#■ >;
#■ <=;
#■ >=;
#■ ==;
#■ !=.

#class Library:
#    def __init__(self, name, address, book_count):
#        self.name = name
#        self.address = address
#        self.book_count = book_count
#
#    def __add__(self, value):
#        self.book_count += value
#    
#    def __iadd__(self, other):
#        self.book_count += other
#        return self
#    
#    def __isub__(self, other):
#        self.book_count -= other
#        return self
#    
#    def __lt__(self, other):
#        if self.book_count < other.book_count:
#            return f'в библиотеке {other.name} книг больше'
#        else:
#            return f'в библиотеке {other.name} книг не больше'
#    
#    def __le__(self, other):
#        if self.book_count <= other.book_count:
#            return f'в библиотеке {other.name} книг не меньше'
#        else:
#            return f'в библиотеке {other.name} книг меньше'
#    
#    def __gt__(self, other):
#        if self.book_count > other.book_count:
#            return f'в библиотеке {other.name} книг меньше'
#        else:
#            return f'в библиотеке {other.name} книг не меньше'
#    
#    def __ge__(self, other):
#        if self.book_count >= other.book_count:
#            return f'в библиотеке {other.name} книг не больше'
#        else:
#            return f'в библиотеке {other.name} книг больше'
#    
#    def __eq__(self, other):
#        if self.book_count == other.book_count:
#            return f'в библиотеках книг одинаково'
#        return f'в библиотеках книг разное количество'
#    
#    def __ne__(self, other):
#        if self.book_count != other.book_count:
#            return f'в библиотеках книг разное количество'
#        return f'в библиотеках книг одинаково'
#    
#lib1 = Library('Библиотека №1', 'г. Жуковский, ул. Чкалова', 23)
#lib2 = Library('Библиотека №2', 'г. Раменское, ул. Cадовая', 23)
#
#print(lib1 == lib2)



#print(lib1.book_count)
#lib1 + 543
#print(lib1.book_count)
#lib1 -= 43
#print(lib1.book_count)

#Создайте класс Date, который будет содержать информацию о дате (день, месяц, год). С помощью механизма
#перегрузки операторов, определите операцию разности
#двух дат (результат в виде количества дней между датами), а также операцию увеличения даты на определенное
#количество дней.