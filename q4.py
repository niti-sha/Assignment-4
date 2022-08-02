# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:30:31 2022

@author: Nitisha Kumari
"""
#Example 4

class NegativeAgeException(RuntimeError):
 	def __init__(self, age):
 		super().__init__()
 		self.age = age
def status(age):
 		if age < 0:
 			raise NegativeAgeException("Only positive integers are allowed")
 		if age>22:
 			print("Eligible for mrg")
 		else:
 			print("not Eligible for mrg....")
try:
 	num = int(input("Enter your age: "))
 	status(num)
except NegativeAgeException:
 	print("Only positive integers are allowed")
except:
    print("something is wrong")
