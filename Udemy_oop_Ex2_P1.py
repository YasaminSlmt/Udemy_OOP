class Fraction:
    def __init__(self, nr, dr = 1):
        if dr < 0:
            dr = -dr
            nr = -nr  
            
        self.nr = nr
        self.dr = dr
        
    def show(self):
        print(self.nr, '/', self.dr)
        
    def multiply(self,f2):
        if isinstance(f2,int):
            f2 = Fraction(f2)
        return Fraction(self.nr*f2.nr , self.dr*f2.dr)
    
    def add(self,f2):
        if isinstance(f2,int):
            f2 = Fraction(f2)
        return Fraction (self.nr*f2.dr + self.dr*f2.nr , self.dr*f2.dr)
        
    def _reduce(self):
        HCF = hcf(self.nr, self.dr)
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