class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self.discount = discount
    
    def display(self):
        print(self.id,  self.marked_price,  self.discount)
        
    @property
    def selling_price(self):
        return self.marked_price * (1 - self.discount/100)

    
p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)