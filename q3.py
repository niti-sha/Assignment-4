# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:29:52 2022

@author: Nitisha Kumari
"""
#Example 3

def status(age):
 	if age < 0:
 		raise ValueError("Only positive integers are allowed")
 	if age>22:
 		print("eligible for mrg")
 	else:
 		print("not eligible for mrg try after some time")
try:
 	num = int(input("Enter your age: "))
 	status(num)
except ValueError:
 	print("Only positive integers are allowed you ......")
finally:
 	print("finally block....")
