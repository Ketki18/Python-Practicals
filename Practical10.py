#!/usr/bin/env python
# coding: utf-8

# 1.  Simple Bike Read System

# In[56]:


class Bike:
    def __init__(self,stock):
        self.stock=stock
    
    def displayStock(self):
        print("Stock available=",self.stock)
            

    def rentBike(self,quan):
        self.quan=quan
        if self.quan>self.stock:
            print("stock not available")
        else:
            self.stock=self.stock-self.quan
            print("Number of bikes given on rent= ",self.quan)
            print("Updated stock= ",self.stock)
    def quit(self):
        print("System Quit")
    
    
b=Bike(500)
while True:
    print("***Bike Read System***")
    print("1-Display Stock Avaiable\n2-Rent on Bike\n3-Quit")
    c=int(input("enter choice no."))
    if c==1:
        b.displayStock()
    elif c==2:
        quan=int(input("enter bikes requirement:- \n"))
        b.rentBike(quan)
    else:
        b.quit()
        break
    
    




        


# 2. A good example to demonstrate multilevel inheritance

# In[59]:


class numbers:
    num1=100
    num2=200
class addition(numbers):
    def add(self):
        add1=self.num1+self.num2
        print("addition=",add1)
class subtraction(addition):
    def sub(self):
        sub1=self.num1-self.num2
        print("Subtraction=",sub1)
n=subtraction()
n.add()
n.sub()
    


# In[ ]:




