# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:53:27 2021

@author: math2
"""

class Order:
    def __init__(self,typ,quantity,price):
        self.typ = typ
        self.quantity = quantity
        self.price = price

class Book:
    def __init__(self,order):
        self.order = order
        
    def insert_buy(self,quantity,price):
        return 0
    
    def insert_sell(self,quantity,price):
        return 0
    
    