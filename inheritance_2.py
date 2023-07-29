# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:51:35 2023

@author: KIIT
"""

class pet():
    def __init__(self,name,color):
        self.name=name
        self.color=color
    
    def run(self):
        print("running")

class Dog(pet):
    
    def say(self):
        print("Bark>>>>>>>>>>>")
        
        
class Cat(pet):
    

    def saye(self):
        print("meow..........")
        
        
class Frink(Dog,Cat,pet):
    def shout(self):
        print("Self calling")
        
        
    def attack(self):
        print("Attacking")
        
        
        
d=Dog("rocket","black")
d.run()
print(d.name)
print(d.color)
d.say()

c=Cat("Runye","white")
c.run()
print(c.color)
print(c.name) 

f=Frink("Reny","Red")
f.shout()
f.attack()
f.say()
f.saye()
f.run()
print(f.name)
print(f.color)

