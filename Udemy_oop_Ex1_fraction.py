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
        