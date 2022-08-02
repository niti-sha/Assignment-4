# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:33:26 2022

@author: Nitisha Kumari
"""
#Example 8

class Person:
 	def __init__(self, first, last):
 		self.firstname = first
 		self.lastname = last
 	def __str__(self):
 		return self.firstname + " " + self.lastname
class Employee(Person):
 def __init__(self, first, last, id):
 		super().__init__(first, last)
 		self.id = id
 def __str__(self):
 		return super().__str__()+" "+self.id
x = Person("kamalpreet", "gurpreet")
y = Employee("kamalpreet", "gurpreet", "111")
print(x)
print(y)
