# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:06:40 2022

@author: Administrator
"""

  
        
class Book:
    def __init__(self,isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies= copies

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,price):
        if 50 < price < 1000:
            self._price = price
        else:
            raise ValueError ('Price cannot be less than 50 or more than 1000')
    
        
    def display(self):
        print("isbn: ", self.isbn, "title: ", self.title,"price: ", self.price,"Copies: ", self.copies )
       
        
    def in_stock(self):
        if self.copies > 0:
            return True
        else:
            return False
            
    def sell(self):
        if self.in_stock():
            self.copies -=1
        else:
            print("The book is out of stock")
        
                
        

book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)
    
    
booklist =[book1, book2, book3, book4]

for book in booklist:
    book.display()
    
    
# use list comprehension to show bookrs written by Jack
[book.title for book in booklist if book.author !='Jack']

