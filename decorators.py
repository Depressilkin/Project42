# Декораторы
#@lru_cache из 
#from functools import lru_cache
#
#@lru_cache
#def f(n):
#    if n <= 1: return 1
#    elif n > 1 and n % 2 == 0: return f(n - 1) *n + f(n - 2) * n
#    else: return f(n - 1) *n + f(n - 2) * n
#
#print(f(45))

#class MyClass:
#    def __init__(self):
#        pass
#
#    @staticmethod
#    def method(a, b):
#        return a, b

#def f2(func):
#    print('декорируемое действие')
#    func()
#    print('второе декорируемое действие')
#
#@f2
#def f1():
#    print('какое-то важное действие')
#
#@f2
#def f3():
#    print('какое-то мало важное действие')
#
##var = f2(f1)
#var2 = f1
#var3 = f3
#print(var2, var3)
#TASK 1
from datetime import datetime
#
#def render():
#    print('*'*10)
#    print(weekday())
#    timer() # создать функцию
#    print('*'*10)
#
#def timer():
#    time = datetime.now()
#    time = time.strftime('%H:%M')
#    print(time)
##TASK 2
#def weekday():
#    today = datetime.today().weekday()
#    week = ['Понедельник','Вторник', "Среда", "Четверг", "Пятница", "Суббота", "Воскресение"]
#    return week[today]
#render()

#TASK 3
#def render(func):
#    print('*'*10)
#    func() # создать функцию
#    print('*'*10)
#
#@render
#def timer():
#    time = datetime.now()
#    time = time.strftime('%H:%M')
#    print(time)
#
#render

#TaSK 4

margo_recipe = ("Маргарита", "томаты", "сыр", "салат", "лук")
cheese_recipe = ("Четыре сыра", "сыр тип 1", "сыр тип 2", "сыр тип 3", "сыр тип 4")
hawaii_recipe = ("Гавайская", "ананасы", "салат", "соус", "сыр", "томаты", "курица", "лук")
kapri_recipe = ("Капричоза", "томатный соус", "моцарелла", "ветчина", "грибы", "артишок", "маслины")
recipe_list =(None, margo_recipe, cheese_recipe, hawaii_recipe, kapri_recipe)

margo_price = 880
cheese_price = 750
hawaii_price = 990
kapri_price = 940
price_list = (None, margo_price, cheese_price, hawaii_price, kapri_price)
ticket = []

print('Добро пожаловать в пиццерай!')
busket = 0
pizza_name = []
while True:
    pizza = int(input('Меню:\n1-Маргарита\n2-Четыре сыра\n3-Гавайская\n4-Капричоза\n0-выход\n'))
    if pizza == 0: break
    ticket += [recipe_list[pizza]]
    pizza_name += [recipe_list[pizza][0]]
    busket += price_list[pizza]
    print(f'Ваш заказ {pizza_name}, на сумму {busket}')
print(f'Ваш заказ {pizza_name}, на сумму {busket}')


def craft(func):
    print('Разогреть печь')
    func()
    print('Достать готовую пиццу!')
    
    
    
@craft
def recipe():
    global ticket
    print("подготовить ингридиенты:")
    for pizz in ticket:
        for i in pizz[1:]:
            print(i)
    print("Выложить ингридиенты на основу пиццы")
    print('Добавить соусы')
    print('Поместить в печь на 40 мин')
