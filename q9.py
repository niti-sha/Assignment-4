# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:33:51 2022

@author: Nitisha Kumari
"""

#Example 9

class Vehicle:
 	def __del__(self):
 		print("Vehicle object destroyed")
 		print(10/0)
v = Vehicle()
del v