#import threading
#def f(a, b):
#    print(a + b)
#    return a + b
#
#def s(a):
#    print(a ** 2)
#    return a ** 2
#thread_1 = threading.Thread(name='Поток первый', target=f, args=(4, 89)) # передача аргументов функции кортежем
#thread_2 = threading.Thread(name='Поток второй', target=s, kwargs=({'a':14}))# передача аргументов функции словарем
#thread_2.start()
#thread_1.start()
#print(thread_1)
#import time
#def counter(t):
#    while t < 8:
#        print(t)
#        time.sleep(t)
#        t += 2
#def welcom(name='None'):
#    while True:
#        print('Welcom,', name)
#        time.sleep(2)
#thread_counter = threading.Thread(name='Thread counter', target=counter, args=(0,))
#thread_welcom = threading.Thread(name='Tread Welcom', target=welcom, kwargs={'name':'Joe'})
#print('Начало программы')
#thread_counter.start()
#print('Середина программы')
#thread_welcom.start()
#thread_counter.join()
#('Конец программы')

#TASK 1
#Пользователь с клавиатуры вводит значения в список.
#После чего запускаются две потока. Первый поток находит максимум в списке. Второй поток находит минимум
#в списке. Результаты вычислений выводятся на экран. 
#import threading
#def stat_num(list=0, mode='max'):
#    if mode != 'max':
#        print('Минимальное значение', min(list))
#    else:
#        print('Максимальное значение', max(list))
#
#
#num = int(input('введите число'))
#list_ = []
#while num != 0:
#    list_.append(num)
#    num = int(input('введите число'))
#thread_max = threading.Thread(name='thread_max', target=stat_num, kwargs={'list':list_, 'mode':'max'})
#thread_min = threading.Thread(name='thread_min', target=stat_num, kwargs={'list':list_, 'mode':'min'})
#
#thread_max.start()
#thread_min.start()
