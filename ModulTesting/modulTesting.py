#MОДУЛЬНОЕ ТЕСТИРОВАНИЕ
#def summ(a, b):
#    return a + b
#
#def test(summ):
#    if summ(2, 2) == 4:
#        return 'Тест прошел успешно'
#    else:
#        return 'Тест провален'   
#print(test(summ), summ(3, 6))

# cлужебное слово assert
#assert условие(condition), сообщение об ошибке(message)
#message = 'Ошибка условия 5 > 7'
#assert 5 > 7, message

#def summ(a, b):
#    return a + b
#
#def test(summ):
#    message = 'Ошибка функции summ'
#    assert summ(2, 2) == 4, message + ' a = 2, b = 2'
#    assert summ(2, -2) == 0, message + ' a = 2, b = -2'
#    assert summ(0, 0) == 0, message + ' a = 0, b = 0'
#    return 'OK'
#
#print(test(summ))

# модуль unittest

#class Calculator:
#    def summ(self, a, b):
#        return a + b
#    def division(self, a, b):
#        return a / b
#    def mult(self, a, b):
#        return a * b 
#
#calc = Calculator()
#print(calc.mult(4, 3))
#print(calc.summ(2, 2))
#print(calc.division(24, 2))
#import unittest

#class TestCalc(unittest.TestCase):
#    def setUp(self):
#        self.calc = Calculator()
#    def test_summ(self):
#        self.assertEqual(self.calc.summ(2, 2), 4)
#        self.assertEqual(self.calc.summ(-2, -2), -4)
#        self.assertEqual(self.calc.summ(-2, 0), -2)
#    
#    def test_division(self):
#        self.assertEqual(self.calc.division(2, 2), 1)
#        self.assertEqual(self.calc.division(-2, -2), 1)
#        self.assertEqual(self.calc.division(0, -2), 0)
#    
#    def test_mult(self):
#        self.assertEqual(self.calc.mult(2, 2), 4)
#        self.assertEqual(self.calc.mult(-2, -2), 4)
#        self.assertEqual(self.calc.mult(0, -2), 0)
import unittest
from main import Frag, CalcFrag
class TestFrag(unittest.TestCase):
    def setUp(self):
        self.frag = Frag(6, 12)
        self.frag2 = Frag(24, 12)
        self.frag3 = Frag(7, 12)
        self.calc_frag = CalcFrag(self.frag2, self.frag3)
    def test_reduction(self):
        self.assertEqual(self.frag.reduction(), (1, 2))
        self.assertEqual(self.frag2.reduction(), (2, 1))
        self.assertEqual(self.frag3.reduction(), (7, 12))
    def test_summ(self):
        self.assertEqual(self.calc_frag.summ(),(31, 12))
    def test_mult(self):
        self.assertEqual(self.calc_frag.mult(),(7, 6))
    def test_division(self):
        self.assertEqual(self.calc_frag.division(), (24, 7))

unittest.main()