# PICKLE and JSON
# PICKLE
# запись в файл dump(что выгрузить, куда выгрузить)
# загрузка из файла load(откуда загрузить)

#class MyClass:
#    def __init__(self, attr1, attr2, attr3):
#        self.attr1 = attr1
#        self.attr2 = attr2
#        self.atrr3 = attr3
#
#from pickle import dump, load
#path = 'C:/Project42/My_File.pkl'
##obj1 = MyClass(23,'Python', [453, 'Hello', True])
#with open(path,'rb') as file:
#    #dump(obj1, file)
#    obj2 = load(file)
#print(obj2.__dict__)
#Создайте класс «Самолет».Наполните его необходимыми характеристиками и методами. 
#Реализуйте упаковку и
#распаковку объектов класса «Самолет» с использованием
#модуля pickle
#from pickle import dump, load, loads
#
#class Airplane:
#    def __init__(self, model, type, class_airplane, passanger, capacity, number_of_engine ):
#        self.model = model
#        self.type = type
#        self.class_airplane = class_airplane
#        self.passanger = passanger
#        self.capacity = capacity
#        self.number_of_engine = number_of_engine
#    def raise_chassi(self):
#        print(f'{self.model} raise chassi')
#    
#    def lower_chassi(self):
#        print(f'{self.model} lower chassi')
#
#    def start_engine(self):
#        print(f'{self.number_of_engine} engine start success!')
#def loader(file):
#    try:
#        while True:
#            yield load(file)
#            
#    except:
#        pass
#
#
#list_airplane = []
#path = 'C:/Project42/Airplane.pkl'
#while True:
#    for airplane in list_airplane:
#        print(airplane.model)
#    choise = input('1 - add aiplane\n2 - save to file\n3 - load from file')
#    if choise == '1':
#        model = input('input model')
#        type =input('input type')
#        class_airplane =input('input class')
#        passanger = input('input passenger')
#        capacity = input('input capacity')
#        number_of_engine = input('input number of engine')
#        airplane = Airplane(model, type, class_airplane, passanger, capacity, number_of_engine)
#        list_airplane.append(airplane)
#    elif choise == '2':
#        with open(path, 'ab') as file:
#            for airplane in list_airplane:
#                dump(airplane,file)
#        list_airplane.clear()
#    elif choise == '3':
#        with open(path, 'rb') as file:
#            for airplane in loader(file):
#                list_airplane.append(airplane)
#

# JSON
# запись в файл dump(что выгрузить, куда выгрузить)
# загрузка из файла load(откуда загрузить)
class MyClass:
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
    
    def toJSON(self): #метод сериализации объекта (подготовка к записи)
        return json.dumps(self, default= lambda obj: obj.__dict__, indent=1, separators=(',', ':'))
import json
path = 'C:/Project42/My_File.json'
#obj1 = MyClass(23,'Python', [453, 'Hello', True])

with open(path,'r') as file:
    #json.dump(obj1.toJSON(), file) # запись в файл
    json_obj2 = json.load(file)
    print(json_obj2)
    dict_obj2 = json.loads(json_obj2)
    obj2 = MyClass(dict_obj2['attr1'], dict_obj2['attr2'], dict_obj2['atrr3'])
    print(obj2)
