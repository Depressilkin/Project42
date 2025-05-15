#SOLID - паттерн проектирования согласно принципам ООП
#S - единственная ответственность у класса (экземпляра класса)
#class Loader:
#    def __init__(self, text, path):
#        self.text = text
#        self.path = path
#    
#    def load(self):
#        with open(self.path, 'w', encoding='utf-8') as file:
#            file.write(self.text)
#
#class Uploader:
#    def __init__(self, path):
#        self.text = ''
#        self.path = path
#    
#    def upload(self):
#        with open(self.path,'r') as file:
#            self.text = file.read()
#        return self.text
    
#text = 'Важный текст'
#path = 'pattern_SOLID/file.txt'
#
#loader = Loader(text, path)
#loader.load()
# O - открытость к расширению, но закрытость к изменению
#from pickle import dump
#class Loader:
#    def __init__(self, text, path):
#        self.text = text
#        self.path = path
#    
#    def load(self):
#        with open(self.path+'.txt', 'w', encoding='utf-8') as file:
#            file.write(self.text)
# расширим функционал класса записью в pikle-файл
#    def load_for_pickle(self, object_load):
#        with open(self.path+'.pkl','wb') as file:
#            dump(object_load, file)
# но не изменяем функционал, при необходимости реализуем его в других классах(объектах) 
#class MyClass:
#    def __init__(self):
#        self.arg = 'Test'
#obj = MyClass()
#text = 'Важный текст'
#path = 'pattern_SOLID/file'
#loader = Loader(text, path)
#loader.load_for_pickle(obj)

#L - принцип замещения Барбары Лисков
#Функционал, логика поведения и т.п. должна легко замещаться от 
# супер-класса к суб-классу и наоборот.

#I - разделения интерфейсов (нет неиспользуемых интерфейсов)
# реализация и использование только необходимых и достаточных функций объекта

#D - инверсия зависимостей. Высокоуровневые классы не зависят от низкоуровневых
#Cм. Пример создания классов Студен->Группа->Академия




