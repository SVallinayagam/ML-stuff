# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:53:55 2019

@author: RPS
"""

class Customer:
    #default constructor
    def __init__(self,fname,lname, balance):
        self.__fname = fname
        self.__lname = lname
        self.__balance = balance
    
    #setters
    def setBalance(self,balance):
       self.__balance=balance
    #Getter
    def getBalance(self):
        return self.__balance
        
customer=Customer("valli","nayagam",1001)
print(customer.getBalance())
print(id(customer))
customer=Customer("valli","nayagam",1001)
print(customer.getBalance())
print(id(customer))