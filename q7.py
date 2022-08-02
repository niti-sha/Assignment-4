# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:33:13 2022

@author: Nitisha Kumari
"""
#Example 7

class Person(object):
 	def __init__(self, first, last):
 		self.firstname = first
 		self.lastname = last
 	def Name(self):
 		return self.firstname + " " + self.lastname
class Employee(Person):
	def __init__(self, first, last, staffnum):
		super().__init__(first,last)
		#Person.__init__(self,first, last)
		self.staffnumber = staffnum
	def GetEmployee(self):
		return self.Name() + ", " + self.staffnumber
x = Person("komal", "addanki")
y = Employee("komal", "addanki", "111")
print(x.Name())
print(y.GetEmployee())
