# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:53:27 2021

@author: math2
"""

### Test Commit

print("Bienvenue dans notre nouveau Projet")

from functools import total_ordering

class Side(enum.Enum):
    BUY = 0
    SELL = 1

class Order:
    compteur=0
    def __init__(self,quantity,price,side):
        self.quantity = quantity
        self.price = price
        self.side=side
        Order.compteur += 1
        self.cpt = Order.compteur
    def __eq__(self,other):
        return other and self.quantity == other.quantity and self.price == other.price
    def __lt__(self,other):
        return other and self.price < other.price
    def __str__(self):
        return "%s %s@%s id=%s" % (self.side.name,self.quantity, self.price,self.cpt)
        


class Book:
    def __init__(self,name):
        self.name = name
        self.buy_orders = []
        self.sell_orders = []
       
    def Tri_book(self):
        self.buy_orders.sort(reverse=True)
        self.sell_orders.sort(reverse=True)
    
    def Affichage_book(self):
        print("Book on ", self.name)
        for s in self.sell_orders:
            if s.quantity!=0: #pas nécessaire
                print("        " + str(s))
        for b in self.buy_orders:
            if b.quantity!=0: #pas nécessaire
                print("        " + str(b))
        print("--------------------------------------")
          
    def Insert_order(self,order):
        if order.side == Side.BUY:
            self.buy_orders.append(order)
        else:
            self.sell_orders.append(order)
        #Affichage
        print("--- Insert ", order.side.name, order.quantity,"@",order.price, "id=", order.cpt, "on", self.name)
        #Test execute
        Book.Match(self,order)
        #Tri + affichage
        Book.Tri_book(self)
        Book.Affichage_book(self)

    def Maximum_Buy(self):
        maxi = 0
        for s in self.buy_orders:
            if s.price > maxi:
                maxi = s.price
        return maxi
    
    def Minimum_Sell(self):
        mini = 10000000
        for s in self.sell_orders:
            if s.price < mini:
                mini = s.price
        return mini
    
    def Match(self,order):
        q = order.quantity
        p = order.price
        if order.side == Side.BUY:
            if p >= Book.Minimum_Sell(self): #on execute
                for b in self.sell_orders:
                    if b.quantity>=q:
                        b.quantity -=q
                        print("Execute",q,"at",b.price,"on", self.name)
                        break
                    else:
                        q -= b.quantity
                        print("Execute",b.quantity,"at",b.price,"on", self.name)                            
                        b.quantity = 0                            
                self.buy_orders.remove(order)
        else: #Sell
            if p <= Book.Maximum_Buy(self):
                for b in self.buy_orders:
                    if b.quantity>=q:
                        b.quantity -=q
                        print("Execute",q,"at",b.price,"on", self.name)
                        break
                    else:
                        q -= b.quantity
                        print("Execute",b.quantity,"at",b.price,"on", self.name)                            
                        b.quantity = 0
                            
                self.sell_orders.remove(order)

                                
                               
    
def Exo1():
    myOb = Book("TEST")
    order1 = Order(10,10.0,Side.BUY)
    myOb.Insert_order(order1)
    order2 = Order(120,12.0,Side.SELL)
    myOb.Insert_order(order2)
    order3 = Order(5,10.0,Side.BUY)
    myOb.Insert_order(order3)
    order4 = Order(2,11.0,Side.BUY)
    myOb.Insert_order(order4)
    order5 = Order(1,10.0,Side.SELL)
    myOb.Insert_order(order5)
    order6 = Order(10,10.0,Side.SELL)
    myOb.Insert_order(order6)
    order6 = Order(10,12.0,Side.BUY)
    myOb.Insert_order(order6)    
    
    
if __name__ == "__main__":
    Exo1()