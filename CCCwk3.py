#!/usr/bin/env python
# coding: utf-8

# ## Lin Crampton, CCC CIS157 Spr21, Prof Stefan Bund ##

# In[1]:
get_ipython().run_line_magic('matplotlib', 'inline')
import cv2
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt


# In[2]:
'''  Problem 7.10.14 Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.  '''
def is_even(n):
#     return bool(not(n%2))
    return False if n%2 else True

for _ in [ -14, -7, 0, 5, 11, 12, 14]:
    print("is_even", _, "returns", is_even(_))


# In[1]:
def is_even(num):
    return bool(not num%2)

assert is_even(5) == False
assert is_even(2) == True


# In[3]:
'''  Problem  7.10.26 Three criteria must be taken into account to identify leap years: It is a leap year if the year is evenly divisible by 4; If the year can be evenly divided by 100, it is NOT a leap year, Unless, the year is also evenly divisible by 400 -- then it is a leap year.  Write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise. '''

def isLeapYear(year):
    if not(year%400): return True
    if not(year%100): return False
    return False if year%4 else True

for _ in [ 1900, 2000, 1996, 2001, 2020, 2021 ]:   
    print("The statement ", _, " is a leap year is ", isLeapYear(_), sep='')


# In[4]:
'''    Problem 8.3 Write a function, is_prime, that takes a single integer argument and returns True when the argument is a prime number and False otherwise.  '''

def isPrime(x):
    if not(x):  return False
    
    # check for integer sqrt if resource contention
    #if  ( (x**(0.5)).is_integer()):   return False   

    for i in range (2, int(x**(0.5))+1):
        if not(x%i):  return False

    return True

for i in [ 1, 2, 5, 7, 11]:
    print("IsPrime for prime number", i, "should return True, and returns", isPrime(i), )
    
for i in [ 0, 27, 12, 21, 49]:
    print("IsPrime for NONprime number", i, "should return False, and returns", isPrime(i), )


# In[13]:
def is_prime(x):

for i in [ 1, 2, 5, 7, 11]:
    print("is_prime for prime number", i, "should return True, and returns", is_prime(i), )
    
for i in [ 0, 27, 12, 21, 49]:
    print("is_prime for NONprime number", i, "should return False, and returns", is_prime(i), )


# In[5]:
''' Problem 7.3     Write a function which is given an exam mark, and it returns a string — the grade for that mark — according to this scheme: The square and round brackets denote closed and open intervals.  A closed interval includes the number, and open interval excludes it.  So 79.99999 gets grade C , but 80 gets grade B.  Test your function by printing the mark and the grade for a number of different marks.'''
def getGrade(grade):

    if grade < 0 or grade > 100:
        return "Error, input out of range"
    
    grades = ['A', 'B', 'C', 'D', 'F']
    scores = [90, 80, 70, 60, 0]
    
    grades_scores = zip(grades, scores)
    for letter_grade, min_score in grades_scores:
        if grade >= min_score:
            return letter_grade
    
    return "Should not be here"

for test_score in [ 89, 78, 69, 35, 101, 234, 58, 90, 80, 70]:
    print("You get an", getGrade(test_score), "for a score of", test_score)


# In[11]:
def getGrade(grade):

for test_score in [ 89, 78, 69, 35, 101, 234, 58, 90, 80, 70]:
    print("You get an", getGrade(test_score), "for a score of", test_score)


# In[6]:
''' Problem 7.6      Write a function findHypot. The function will be given the length of two sides of a right-angled triangle and it should return the length of the hypotenuse. 
Hint: x ** 0.5 will return the square root, or use sqrt from the math module'''
def findHypot(a,b):
    return round((a**2+b**2)**(0.5),1)

aa=[10, 20, 5, 10, 121, 15, 16, 12, 14, 21]
bb=[10, 20, 25, 100, 11, 30, 4, 5, 48,72]
for a,b in zip(aa,bb):
    print("For a right triangle with sides", a, "and", b, "the hypoteneuse is", findHypot(a,b))


# In[7]:
'''   Problem 8.2   
Write a function print_triangular_numbers(n) that prints out the first n triangular numbers.  A call to print_triangular_numbers(5) would produce the following output:
1       1
2       3
3       6
4       10
5       15'''

def print_triangular_numbers(n):
    for i in range(1,n+1):
        print(i, "\t", (i*(i+1)//2))
       
print_triangular_numbers(5)


# In[8]:
'''   Problem 8.15   Research the Sobel edge detection algorithm and implement it.  
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

img = cv2.imread(cv2.samples.findFile("luther.jpg"))
if img is None:
    sys.exit("Cannot read input image")
original=img

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

sobel = cv2.bitwise_or(sobelX, sobelY)

titles = ['Original', 'Sobel Edge Enhanced']
images = [original, sobel]
for i in [0,1]:
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
