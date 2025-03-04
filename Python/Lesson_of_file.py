#C:\Users\Teacher\Documents\Python42
#открытие потока функция open('полное_имя_файла', режим открытия)
#режим r - режим чтения (rt - чтение в текстовой форме, rb - чтение в двоичной форме)
#режим w - режим запись (wt - запись в текстовой форме, wb - запись в двоичной форме)
#режим a - режим добавления (at - добавления в текстовой форме, ab - добавления в двоичной форме)
#закрытие потока close()
#from os import strerror
#try:
#    file = open('C:/Users/Teacher/Documents/Python42/textt.txt')
#    file.close()
#    print(file)
#except IOError as e:
#    print(f'Файл не найден {strerror(e.errno)}')
# конструкция with ... as ...:
##считывание файла
#try:
#    with open('C:/Users/Teacher/Documents/Python42/text.txt', 'r') as file:
#        #text = file.readlines()#считать строки        #readline()считать строку    #read(2)считать всё
#        #print(text)
#        for line in file:
#            print(type(line))
#except IOError as e:
#    print(f'Файл не найден {strerror(e.errno)}')
#print('конец программы')

###запись файла
#try:
#    with open('C:/Users/Teacher/Documents/Python42/text.txt', 'w') as file:
#        file.write('Text from change')
#except IOError as e:
#    print(f'Файл не найден {strerror(e.errno)}')
###добавление файла
#try:
#    with open('C:/Users/Teacher/Documents/Python42/text.txt', 'a') as file:
#        file.write('\nNew content')
#except IOError as e:
#    print(f'Файл не найден {strerror(e.errno)}')
##создание файла
#try:
#    with open('C:/Users/Teacher/Documents/Python42/text2.txt', 'w') as file:
#        file.write('Text from change')
#except IOError as e:
#    print(f'Файл не найден {strerror(e.errno)}')
#перебор символов в файле
#try:
#    with open('C:/Users/Teacher/Documents/Python42/text.txt','r') as f:
#        counter = 0
#        letter = f.read(1)
#        while letter != '':
#            counter += 1
#            print(letter)
#            letter = f.read(1)
#except IOError as err:
#    print(strerror(err.errno))
#print(f'Количество символов в файле {counter}')

#Дан текстовый файл. Необходимо создать новый файл,
#в который требуется переписать из исходного файла все
#слова, состоящие не менее чем из семи букв.
from os import strerror
#1 открыть и считывать (read)
#try:
#    with open('C:/Users/Teacher/Documents/Python42/text.txt', 'r') as f:
#        text = f.read()
#    word = ''
#    words_list = []
#    index = 0
#    for letter in text:
#        if letter not in ' ,!.;?\\' or (text[index - 1] != "" and letter == 'n'):
#            word += letter.strip()
##2 поиск слов(циклом, список)
#        elif len(word) > 6:
#            words_list.append(word)
#            word = ''
#        index += 1
#    print(words_list)
##3 записывать слова в файла по условию 
#    with open('C:/Users/Teacher/Documents/Python42/text2.txt', 'a') as f:
#        for i in words_list:
#            f.write(i + ' ')
#except IOError as er:
#    print(strerror(er.errno))
#Дан текстовый файл. Необходимо переписать его
#строки в другой файл. Порядок строк во втором файле
#должен совпадать с порядком строк в заданном файле.
#from os import strerror
#try:
#    with open('C:/Users/Teacher/Documents/Python42/text.txt', 'r') as f:
#        for line in f:
#            with open('C:/Users/Teacher/Documents/Python42/text2.txt', 'a') as f2:
#                f2.write(line)
#except IOError as er:
#    print(strerror(er.errno))


#Дан текстовый файл. Необходимо переписать его
#строки в другой файл. Порядок строк во втором файле
#должен быть обратным по отношению к порядку строк
#в заданном файле.from os import strerror
#try:
#    with open('C:/Users/Teacher/Documents/Python42/text.txt', 'r') as f:
#        lines_list = []
#        for line in f:
#            lines_list.insert(0, line)
#        with open('C:/Users/Teacher/Documents/Python42/text2.txt', 'a') as f2:
#            for line in lines_list:
#                f2.write(line)
#        
#except IOError as er:
#    print(strerror(er.errno))
#Дан текстовыйфайл.Добавить в него строку из двенадцати звездочек (************), поместив ее после последней
#из строк, в которых нет запятой. Если таких строк нет,
#то новая строка должна быть добавлена после всех строк
#имеющегося файла. Результат записать в другой файл.
#
#try:
#    with open('C:/Users/Teacher/Documents/Python42/text.txt', 'r') as f:
#        text = f.readlines()
#        index_line = len(text) - 1
#        for line in range(len(text) -1 , -1, -1):
#            if ',' in text[line]:
#                index_line = line
#                break
#        with open('C:/Users/Teacher/Documents/Python42/text2.txt', 'a') as f2:
#            for line in range(len(text)):
#                if index_line == line:
#                    f2.write(text[line] + 12 * '*' + '\n')
#                else:
#                    f2.write(text[line])
#
#
#
#
#        
#except IOError as er:
#    print(strerror(er.errno))
#from os import strerror
#try:
#    list_data = []
#    with open('Data.csv') as file:
#        for i in file:
#            name, last_name, age = i.split(';')
#            list_data.append([name, last_name, age])
#    list_data = list_data[1:]
#    for i in list_data:
#        i[2] = int(i[2])
#    print(list_data)
#except IOError as e:
#    print(strerror(e.errno))

#Задание 5
#Дан текстовый файл. Подсчитать количество слов,
#начинающихся с символа, который задаёт пользователь.
#letter_search = input('Введите букву для поиска слов')
#from os import strerror
#try:
#    with open('text.txt') as file:
#        text = []
#        count = 0
#        for i in file:
#            text += i.split(' ')
#        print(text)
#        for i in text:
#            if i[0].lower() == letter_search:
#                count += 1
#        print(count)
#        
#except IOError as e:
#    print(strerror(e.errno))

#Задание 6
#Дан текстовый файл. Переписать в другой файл все его
#строки с заменой в них символа * на символ & и наоборот.from os import strerror
#try:
    #with open('text.txt') as file:
    #    with open('text2.txt','a') as file2:
    #        letter = file.read(1)
    #        while letter != '':
    #            if letter == 'a':
    #                file2.write('*')
    #            else:
    #                file2.write(letter)
    #            letter = file.read(1)
#    with open('text.txt') as file:
#        text = file.read()
#        text = text.replace('a', '*')
#    with open('text2.txt','a') as file2:
#        file2.write(text)
#        
#except IOError as e:
#    print(strerror(e.errno))

#Задание 7
#Дан массив строк. Записать их в файл, расположив
#каждый элемент массива на отдельной строке с сохранением порядка
#array = ['$' * i for i in range(1, 11)]
#print(array)
#try:
#    with open('text2.txt', 'a') as file:
#        for i in array:
#            file.write(i + '\n')
#except IOError as e:
#    print(strerror(e.errno))
#
#    Задание 9
#Дан текстовый файл. Подсчитать количество символов в нём.
#Задание 10
#Дан текстовый файл. Подсчитать количество строк
#в нём.

#try:
#    with open('text.txt', 'r') as file:
#        count_line = 0
#        count_symbol = 0
#        for i in file:
#            print(i)
#            count_line += 1
#            count_symbol += len(i)
#        print(count_line, count_symbol)
#except IOError as e:
#    print(strerror(e.errno))
#Задание 1
#Дан текстовыйфайл. Необходимо создать новый файл
#убрав из него все неприемлемые слова. 
#Список неприемлемых слов находится в другом файле
#try:
    ##1
    #with open('text2.txt', 'r') as file:
    #    list_diss = []
    #    list_word = []
    #    for i in file:
    #        list_diss.append(i.strip().lower())
    ##2
    #with open('text.txt', 'r') as file:
    #    for i in file:
    #        i = i.strip().lower()
    #        list_word += i.split(' ')
    #for i in range(len(list_word)):
    #    if list_word[i][-1] in '!.,?:;"\')':
    #        list_word[i] = list_word[i][:-1]
    #print(list_word)
    ##3
    #for word_diss in list_diss:
    #    while word_diss in list_word:
    #        list_word.remove(word_diss)
    #print(list_word)
    #text = ' '.join(list_word)
#
#    #1
#    with open('text2.txt', 'r') as file:
#        list_diss = []
#        for i in file:
#            list_diss.append(i.strip().lower())
#    #2
#    with open('text.txt', 'r') as file:
#        text = file.read()
#    
#    #3
#    for word_diss in list_diss:
#        text = text.replace(word_diss, '')
#        text = text.replace(word_diss.title(), '')
#    
#    print(text)
#    with open('content.txt', 'w') as file:
#        file.write(text)

