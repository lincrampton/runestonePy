#!/usr/bin/env python
# coding: utf-8

# ## Homework Week 1
# Lin Crampton, CCC CIS157, Stefan Bund

# In[1]:
'''1.1  Evaluate the following numerical expressions in your head, then use the active code window to check your results:''' 
print("Five squared =", 5 ** 2)
print("9 x 5 =", 9 * 5)
print("15 divided by 12 =", 15 / 12)
print("12 divided by 15 =", 12 / 15)
print("Integer portion of 15 divided by 12 =", 15 // 12)
print("Integer portion of 12 divided by 15 =", 12 // 15)
print("5 mod 2 =", 5 % 2)
print("9 mod 5 =", 9 % 5)
print("15 mod 12 =", 15 % 12)
print("12 mod 15 =", 12 % 15)
print("6 mod 6 =", 6 % 6)
print("0 mod 7 =", 0 % 7)


# In[2]:
'''1.2 What is the order of the arithmetic operations in the following expression. Evaluate the expression by hand and then check your work.'''
print(eval("2 + (3 - 1) * 10 / 5 * (2 + 3)"), " is the computer's evaluation.")


# In[3]:
'''1.3 Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).  If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).  Write a Python program to solve the general version of the above problem.  Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm.  Your program should output what the time will be on the clock when the alarm goes off.'''
time_now = int(input('Please enter the current time: '))
time_then = int(input('Please enter hours elapsed: '))
print("If the clock could talk, it would say", (time_now+time_then) % 12)


# In[4]:
'''1.4 It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday.  If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6) Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.'''
depart_day = int(input('Please enter your departure day as an integer: '))
vacay_len = int(input('Please enter the number of days you plan on being on vacation'))
print('I predict you will return on day #', (depart_day+vacay_len)%7,sep='')


# In[3]:
'''1.5 Take the sentence: All work and no play makes Jack a dull boy. 
Store each word in a separate variable, then print out the sentence on one line using print.'''
working_line = "All work and no play makes Jack a dull boy."
words = working_line.split()
print("Examples of individual words stored in a variable would be the first and last words:", words[0], words[-1])
print('And the complete sentence would be ...')
print(" ".join(words))

import re
words_in_line = re.findall(r'\w+', working_line)
print(" ".join(words_in_line))


# In[6]:
'''1.6 Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.'''
print("6*1 -2 should equal 4, and does equal", 6*1-2)
print("6 * (1-2) should equal -6, and does equal", eval("6*(1-2)"))


# In[7]:
'''1.7 The formula for compound interest, A=P(1+r/n)**nt Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08).  Then have the program prompt the user for the number of years, t, that the money will be compounded for.  Calculate and print the final amount after t years.''' 
P, n, r = 10000, 12, 0.08
t = int(input("Please input number of years to hold asset:"))
final_value =  P * ((1 + r/n)**(n*t))
print("The final value of your investment is ${:0.2f}.".format(final_value), sep='')


# In[8]:
'''1.8 Write a program that will compute the area of a circle.  Prompt the user to enter the radius and print a nice message back to the user with the answer.''' 
import math
radius = float(input('Please enter a value for radius: '))
print("The area of a circle with radius",radius,'is', radius**2 * math.pi)


# In[9]:
'''1.9 Write a program that will compute the area of a rectangle.  Prompt the user to enter the width and height of the rectangle.  Print a nice message with the answer.'''
height = float(input('Please enter the height of your rectangle:'))
width = float(input('Please enter the width of your rectangle:'))
print('Your rectangle has an area of :', height*width)


# In[11]:
'''1.10 Write a program that will compute MPG for a car.  Prompt the user to enter the number of miles driven and the number of gallons used.  Print a nice message with the answer.'''
miles = float(input('Please enter the number of miles driven:'))
gallons = float(input('Please enter the number of gallons of gas consumed:'))
print('Your car gets', miles/gallons, 'mpg')


# In[10]:
'''1.11 Write a program that will convert degrees celsius to degrees fahrenheit.'''
C = float(input('The temperature in degress celsius is: '))
F = (C* 9/5) + 32
print('The temerature in degres fahrenheit is: ', F)


# In[13]:
'''1.12 Write a program that will convert degrees fahrenheit to degrees celsius.'''
F = float(input('The temperature in degress fahrenheit is: '))
C = (F-32)/1.8
print('The temerature in degres celsius is: ', C)
