# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:32:39 2022

@author: Nitisha Kumari
"""
#Example 6

try:
    print("outer try block")
    n = int(input("enter a number"))
    print(10/n)
    try:
        print("inner try")
        print("anu"+"preet")
    except TypeError:
        print("Hello")
    else:
        print("inner no exception")
except ArithmeticError:
    print(10/5)
else:
    print("outer no excepiton")
finally:
    print("finally block") 
