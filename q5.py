# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:31:15 2022

@author: Nitisha Kumari
"""
#Example 5:

class TooYoungException(Exception):
 def __init__(self,age):
 		self.age=age
class TooOldException(Exception):
    def __init__(self,age):
        self.age=age
try:
    age=int(input("Enter Age:"))
    if age<18:
        raise TooYoungException("Plz wait some time ")
    elif age>65:
        raise TooOldException("Your age too old")
    else:
        print("we will find one girl soon")
except TooYoungException as e:
 	print("Plz wait some time ")
except TooOldException as e:
 	print("Your age too old ")

