class Fraction:
    def __init__(self, nr, dr = 1):
        if dr < 0:
            dr = -dr
            nr = -nr  
            
        self.nr = nr
        self.dr = dr
        
    def show(self):
        print(f'{self.nr} / {self.dr}')
        
    def multiply(self,f2):
        if isinstance(f2,int):
            f2 = Fraction(f2)
        f = Fraction(self.nr*f2.nr , self.dr*f2.dr)
        f._reduce()
        return f
    
    def add(self,f2):
        if isinstance(f2,int):
            f2 = Fraction(f2)
            
        f = Fraction (self.nr*f2.dr + self.dr*f2.nr , self.dr*f2.dr)
        f._reduce()
        return f
        
    def _reduce(self):
        HCF = self.hcf(self.nr, self.dr)
        if HCF == 0:
            return
        
        self.nr = self.nr / HCF
        self.dr = self.dr / HCF
        
        
        
        
        
        
    @staticmethod
    def hcf(x,y):
        x = abs(x)
        y = abs(y)
        
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x%s == 0 and y%s == 0:
                break
            s -=1
        return s
    
    
    
    
f1 = Fraction(6,36)
f1.show()
f2 = Fraction(2,-12)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3 = f1.add(5)
f3.show()
f3 = f1.multiply(5)
f3.show()
