# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:53:27 2021

@author: math2
"""

### Test Commit

print("Bienvenue dans notre nouveau Projet")

class Order:
    compteur=0
    def __init__(self,quantity,price):
        self.quantity = quantity
        self.price = price
        Order.compteur += 1
        self.cpt = Order.compteur

class Book:
    def __init__(self,name):
        self.name = name
        self.bookorder = []
    
    def Affichage(self,typ,order):
        print("--- Insert ", typ, order.quantity,"@",order.price, "id=", order.cpt, "on", self.name)
     
    def AffichageBook(self,typ,order):
        print("Book on", self.name)
        n = len(self.bookorder)
        for i in range(n):
            print("     ",typ,self.bookorder[i].quantity,"@",self.bookorder[i].price, "id=", self.bookorder[i].cpt)
        print("-----------------------------------")
                   
    def insert_buy(self,order):
        self.bookorder.append(order)
        Book.Affichage(self,"BUY",order)
        Book.AffichageBook(self,"BUY",order)
    
    def insert_sell(self,order):
        self.bookorder.append(order)
        Book.Affichage(self,"SELL",order)
        Book.AffichageBook(self,"SELL",order)
        
    
        
if __name__ == "__main__":
    myfirstorder = Book("TEST")
    order1 = Order(10,10.0)
    myfirstorder.insert_buy(order1)
    order2 = Order(120,12.0)
    myfirstorder.insert_sell(order2)