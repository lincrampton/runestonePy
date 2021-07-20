#!/usr/bin/env python
# coding: utf-8

# ## Homework Week 6
# 
# Lin Crampton, CCC CIS157, Stefan Bund

# In[1]:
'''   Problem 13.10 Write a function named readposint that uses the input dialog to prompt the user for a positive integer and then checks the input to confirm that it meets the requirements. It should be able to handle inputs that cannot be converted to int, as well as negative int, and edge cases (e.g. when the user closes the dialog, or does not enter anything at all.)'''

def readposint():
    while True:
        try:
            raw = input("Please enter a positive integer: ")
            n = int(raw)
            if n<=0: raise ValueError
            break
        except ValueError:
            print("\n", raw, "is not a valid positive integer")
    return n
readposint()


# In[2]:
'''  Problem 16.8.2 Write a recursive function to compute the factorial of a number.'''
def computeFactorial(n):
    if n < 2: 
        return 1
    else:
        return n * computeFactorial(n-1)

def easyFactorial(n):
    import math
    return math.factorial(n)

test_cases = [7, 1, 2, 4, 0, 9]
for x in test_cases:
    assert computeFactorial(x) == easyFactorial(x)
print('factorial 0 should be 1 and is', easyFactorial(0))
print('factorial 5 should be 120 and is', computeFactorial(5))


# In[3]:
'''  Problem 16.8.4  Write a recursive function to reverse a list.'''
def reverseList(lst):
    if not lst: return []
    return [lst[-1]] + reverseList(lst[:-1])

linzList = ['a', 'b', 'c', 1, 2, 3]
print('abc123 reversed is', reverseList(linzList))


# In[4]:
'''  Problem 16.8.10 Write a recursive function to compute the Fibonacci sequence.  How does the performance of the recursive function compare to that of an iterative version?'''

def recFibo(n):
    if n==0: return 0
    if n==1 or n==2: return 1
    return recFibo(n-1) + recFibo(n-2)


def dpFibo(n, dp_dict={1:1,2:1}):
    if n==0 or n==1:return n
    if n not in dp_dict:
        dp_dict[n] = dpFibo(n-1,dp_dict) + dpFibo(n-2,dp_dict)
    return dp_dict[n]


def fibo(n):
    if n==0 or n==1:return n
    a,b = 1,1
    for _ in range(2,n): 
        a, b = b, a+b
    return b

    
from timeit import timeit

trials=700
fibo_N = 9
plain_speed = timeit(lambda:fibo(fibo_N), number=trials) 
recursive_speed = timeit(lambda:recFibo(fibo_N), number=trials) 
dynamic_speed = timeit(lambda:dpFibo(fibo_N), number=trials) 

for N in [ 4, 1, 11, 7, 0]:
    assert fibo(N) == recFibo(N) == dpFibo(N)


print("-=- Relative Speed of Different Algorithms -=-")
print(plain_speed, "= regular Fibonacci w", trials, "runs, getting the Fibonacci seq value for N =", fibo_N)
print(recursive_speed, "= recursive algo for Fibonacci w", trials, "runs, getting the Fibonacci seq value for N =", fibo_N)
print(dynamic_speed, "= dynamic programming Fibonacci w", trials, "runs, getting the Fibonacci seq value for N =", fibo_N)

