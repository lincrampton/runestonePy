#!/usr/bin/env python
# coding: utf-8

# ## Homework Week 2, Chapters 5 & 6
# Lin Crampton, CCC CIS157 Spr21, Prof Stefan Bund

# In[1]:
'''        Chapter 5, Problem 17        
Print 10 random numbers between 25 and 35, inclusive.'''

import random
print("Can generate 10 numbers using randrange in a for-loop:")
for _ in range(10):
    print("\t", random.randrange(25,36))
print('\nOr generate a list using random.randrange and print it: ')
rand_list = [random.randrange(25,36) for x in range(10)]
print(rand_list)
print("\nOr just use random.sample:  ", random.sample(range(25,36), 10))


# In[2]:
'''        Chapter 5, Problem 18      
The Pythagorean Theorem tells us that the length of the hypotenuse of a right triangle is related to the lengths of the other two sides. Look through the math module and see if you can find a function that will compute this relationship for you.  Once you find it, write a short program to try it out.
'''
import math
print("A 3/4/5 triangle is special. So if I input 3 and 4, I should get", math.hypot(3,4))
print("A 5/12/13 triangle is special. So if I input 5 and 12, I should get", math.hypot(5,12))


# In[3]:
'''        Chapter 6, Problem 6.7        Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and including n. E.g., sumTo(10) would be 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2.'''

def sumTo(n):
    return n * (n+1)/2

print("sumTo of 10 should be 55 and is: ", int(sumTo(10)))
print("sumTo of 15 should be 120 and is: ", int(sumTo(15)))
print("sumTo of 0 should be 0 and is: ", int(sumTo(0)))
print("sumTo of 25 should be 325 and is: ", int(sumTo(25)))
print("sumTo of 7 should be 28 and is: ", int(sumTo(7)))


# In[2]:
'''        Chapter 6, Problem 6.8        Write a function areaOfCircle(r) to return the area of a circle of radius r.  Make sure you use the the math module as part of your solution.'''

def areaOfCircle(r):
    from math import pi
    return pi * r**2
print("The area of a circle of radius 1 should be approx 3.14 and is {:0.5f}.".format(areaOfCircle(1)))
print("The area of a circle of radius 2 should be approx 12.5 and is {:0.5f}.".format(areaOfCircle(2)))


# In[11]:
'''     Chapter 5, Problem 18 Search on the internet for a way to calculate an approximation for pi. There are many that use simple arithmetic. Write a program to compute the approximation and then print that value as well as the value of math.pi from the math module.'''
from math import pi  # no need to import entire math library for one constant

def pi_accuracy(x): # determine the percentage closeness/accuracy of a pi approximation to math.pi
    mean_pi = (x + pi)/2
    return abs((pi - x)/mean_pi) * 1

def pi_difference(x): # determine the absolute closeness/accuracy to a pi approximation to math.pi
    return abs(pi - x)

# Using real simple math as approximation to pi, per https://www.mathsisfun.com/numbers/pi.html from math import pi  
# no need to import entire math library for one constant
print("Using 355/113 approximation to pi is {:0.9f}; math.pi is {:0.9f}.".format(355/113,pi))
print("These numbers differ by ", pi_difference(355/113),",", sep='')
print("which is a ", pi_accuracy(355/113), "% difference", sep='')

