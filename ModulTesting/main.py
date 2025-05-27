class CalcFrag:
    def __init__(self, frag1, frag2):
        self.frag1 = frag1
        self.frag2 = frag2
    
    def summ(self):
        numerator = self.frag1.numerator * self.frag2.denominator + self.frag2.numerator * self.frag1.denominator
        denominator = self.frag1.denominator * self.frag2.denominator
        frag = Frag(numerator, denominator)
        frag.reduction()
        return frag.numerator, frag.denominator
    
    def mult(self):
        numerator = self.frag1.numerator * self.frag2.numerator
        denominator = self.frag1.denominator * self.frag2.denominator
        frag = Frag(numerator, denominator)
        frag.reduction()
        return frag.numerator, frag.denominator
    
    def division(self):
        numerator = self.frag1.numerator * self.frag2.denominator
        denominator = self.frag1.denominator * self.frag2.numerator
        frag = Frag(numerator, denominator)
        frag.reduction()
        return frag.numerator, frag.denominator
    
class Frag:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def reduction(self):
        nod = 1
        for delet in range(2, min(self.numerator, self.denominator) + 1):
            if self.numerator % delet == 0 and self.denominator % delet == 0:
                nod = delet
        self.numerator = self.numerator // nod
        self.denominator = self.denominator // nod
        return self.numerator, self.denominator
        

        