"""
# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) local -> Enclosed -> Global -> Built-in
"""

def func1():
    x = 1 # variable local in func1
    print(x)

def func2():
    x = 2 # variable local in func2
    print(x)

x = 3 # variable global

func1()
func2()

# Built-in
from math import e

def func3():
    print(e)

func3()