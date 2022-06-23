class Circle:
    def __init__(self,radius):
       self._radius = radius

    @property    
    def area(self):
        return 3.14 * self.radius**2
    @property
    def radius(self):
        return self._radius 
    
    @radius.setter
    def radius(self,new_radius):
        if new_radius > 0:
            self._radius = new_radius
        else:
            raise ValueError('Radius should be positive')
    @property
    def diameter(self):
        return 2 * self.radius
    @property
    def circumference(self):
        return 3.14 * self.diameter
    
    
c1 = Circle(7)
print( c1.radius, c1.diameter, c1.circumference, c1.area )