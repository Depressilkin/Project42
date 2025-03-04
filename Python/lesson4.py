
"""## Cоздание списка"""

#1
#category = ['Drama', 'Comedy', 'Fantasy']
#category2 = []
##2 с помощью функции list
#courses = list(('Math', 'Algorithms', 'Database'))
#courses2 = list()
#print(category)
#print(courses)
#d = [43, 34.6, 'Hello', True, [34, 'World'], 43]
#var = 'Hello'
#d = list(var)
#print(d)
#3 генератор списков
#newList = [выражение for элемент in последовательность]
#newList - имя генерируемого списка, выражение - выражение, которое
#выполняется над каждым элементом, элемент - элемент последовательности
#list1 = [i * 2 for i in range(10) if i % 2 == 0]
#print(list1)
#name = ['Anna', 'Joe', 'Mike', 'John']
#new_Name = [ i for i in name if i != 'Mike']
#print(new_Name)
#list3 = [[i for i in range(3)] for y in range(5)]
#print(list3)
from random import randint
num_ticket = [randint(1, 90) for i in range(15)]
print(num_ticket)

#TODO
#for symb in ['.', '!', '?']:
#    new_s = s.split(symb)
#    print(new_s)
#    for i in range(len(new_s)):
#        if  i > 0 and i < len(new_s) - 1:
#            new_s[i] = new_s[i].replace(new_s[i][1], new_s[i][1].upper(), 1)
#    new_s = symb.join(new_s)
#print(new_s)

"""##Индексация и срезы"""

d = [43, 34.6, 'Hello', True, [34, 'World'], 43, 657]
# Cрез
# имя_коллекции[начало:конец(без_учета):шаг]
print(d[1])
print(d[-1])
print(d[1:3])
print(d[::2])
print(d[len(d)-1])

"""## Функции списков"""

d = [43, 34.6, 43, 657]
print(len(d)) #4
print(max(d)) #657
print(min(d)) # 34.6
print(sum(d)) # 777.6
print(sorted(d)) # 34.6 43 43 657
print(sorted(d, reverse = False))
print(d)
d.sort()
print(d)

#Задание 2 Пользователь с клавиатуры вводит элементы списка целых и
# некоторое число. Необходимо посчитать сколько раз данное
#число присутствует в списке. Результат вывести на экран.
from random import randint
l = [ randint(1, 100) for i in range(50)]
print(l)
s = int(input('Введите число для поиска'))
#1
counter = 0 # объявление переменной для счета вхождения числа
for i in range(len(l)): # for i in l: цикл для перебора чисел из списка
  if s == l[i]: # if s == i: условие введенное число есть в списке
    counter += 1
print(counter)

#Задание 3 Пользователь с клавиатурывводит элементы списка целых.
#Необходимо посчитать сумму всех элементов и их среднеарифметическое.
#Результаты вывести на экран.
from random import randint
l = [ randint(1, 10) for i in range(10)]
print(l)
#1
summ = 0
counter = 0
for i in l: # for i in range(len(l))
  summ += i
  counter += 1
print(summ, summ / counter)
#2
print(sum(l), sum(l)/len(l))

list_ = ['a', 'ab', 'bb', 'ac', 4]
list2 = ['a', 'ab', 'bb', 'ac']
print(sorted(l))

"""## Методы списков"""

category = ['Drama', 'Comedy', 'Fantasy']
# добавление
category.append('Anime')
print(category)
category.insert(1, 'Horror') #insert(индекс_куда_добавить, Что_добавить)
print(category)

# удаление
category.pop(1) #pop(индекс_удаляемого)
print(category)
category.append('Comedy')
category.remove('Comedy')
print(category)
category2 = category.copy()
category2.clear()
print(category2)
# индексация
print(category)
print(category.index('Anime'))
# подсчет вхождений
print(category.count('Anime'))

category = ['Drama', 'Comedy', 'Fantasy']
category2 = category
category2.append('Crime')
print(category)
print(category2)
print(category is category2)

#category2 = category.copy()
#print(category is category2)
category2 = category[:]
print(category is category2)

a = 5
b = a
b -= 1
print(b)

"""## Матрица (список в списке)"""

# Матрица (список в списке)
from random import randint
list_matrix = [[randint(1,10) for x in range(5)] for y in range(5)]
print(list_matrix)
for i in list_matrix:
  for y in i:
    print(y, end=' ')
  print(' ')
print(list_matrix[1][2])

"""Создать журнал для 4 студентов, у каждого студента записано имя и 4 оценки, найти среднюю оценку каждого студента"""

journal = [['Joe', 6, 10 , 6, 8], ['Max', 12, 10 , 4, 5, 9, 8], ['Anna', 6, 7 , 6, 4], ['Lee', 12, 11 , 12, 11]] # список
for student in journal: # перебор студентов
  print(student)
  summ = 0 # для суммы оценок
  count = 0 # для количества оценок
  for i in range(len(student)): #перебор оценок студента
    if i > 0: # условие, что это не имя , не [0] элемент
      summ += student[i] # сумма оценок
      count += 1 # количество оценок
  print(student[0], summ / count) #вывод имени и среднего балла