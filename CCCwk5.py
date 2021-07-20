#!/usr/bin/env python
# coding: utf-8

# ## Homework Week 5  
# 
# Lin Crampton, CCC CIS157, Stefan Bund

# In[1]:
''' Problem 11.1   
The following sample file called studentdata.txt contains one line for each student
in an imaginary class. The student’s name is the first thing on each line, followed
by some exam scores. The number of scores might be different for each student.
Using the text file studentdata.txt write a program that prints out the names of 
students that have more than six quiz scores.'''

my_dict = {}

with open("student_data.txt", 'r') as f:
    for line in f:
        items = line.split()
        key, values = items[0], items[1:]
        my_dict[key] = values
        if len(values) > 6:
            print("Students with more than six data items:")
            print("\t",key, values)
# print("\n\n",my_dict)


# In[11]:
f = open("studentdata.txt", "r")

for aline in f:
    items = aline.split()
#     if len(items[2:]) > 5:
#         print(items[0])
    if len(items) > 7:
        print(items[0])
f.close()

print(items)
print(items[2:])


# In[2]:
'''  Problem 11.2
Using the text file studentdata.txt (shown in exercise 1) write a program
that calculates the average grade for each student, and print out the 
student’s name along with their average grade.'''
my_dict = {}

with open("student_data.txt", 'r') as f:
    for line in f:
        items = line.split()
        key, values = items[0], items[1:]
        values = [int(i) for i in values]
        print(key, " had an average score of ", sum(values)/len(values), sep='') 


# In[3]:
'''  Problem 11.3  
Using the text file studentdata.txt (shown in exercise 1) write a program that
calculates the min and max score for each student. Print out their name as well.'''

my_dict = {}

with open("student_data.txt", 'r') as f:
    for line in f:
        items = line.split()
        key, values = items[0], items[1:]
        print(key, ':\t max score=', max(values), "\tmin score=", min(values),sep='')


# In[4]:
'''  Problem 11.4   
Here is a file called labdata.txt that contains some sample data from a lab experiment.   
Interpret the data file labdata.txt such that each line contains a an x,y coordinate pair.'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

# with open('labdata.txt','r') as f:
#     X,Y = zip(*[l.split() for l in f])
# print(X)

data = pd.read_csv("labdata.txt", header=None, delim_whitespace=True)
X = data.iloc[:, 0].values.reshape(-1, 1)
Y = data.iloc[:, 1].values.reshape(-1, 1)
linear_regressor = LinearRegression() 
linear_regressor.fit(X, Y) 
Y_pred = linear_regressor.predict(X).tolist()
plt.plot(X, Y_pred, color='red', label='best fit')
plt.plot(X, Y_pred-np.std(Y), color='yellow', label='standard deviation')
plt.plot(X, Y_pred+np.std(Y), color='yellow')
# plt.fill_between(range(100), YlessSD, YplusSD, color='yellow', alpha=0.2)
plt.scatter(X, Y, label='data points')
plt.title("Lab Data")
plt.legend(bbox_to_anchor=(1.05, 0.35), frameon=False)
plt.show()


# In[5]:
'''  Problem 12.1 Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs.  Case should be ignored:'''

import re

counts = {}
astring = input('Please enter a sentence: ')
astring = (re.sub(r'\W+', '', astring)).upper()
for char in astring:
    if char.isalpha():
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
print("The dictionary of the letters in the sentence you entered is: ", sorted(counts.items()))

from collections import Counter
test_str = input('\nPlease enter a sentence: ')
test_str_alpha = re.sub(r'\W+', '', test_str)
print("Using Counter is so much easier.  And the letters are:", sorted(Counter(test_str_alpha.upper()).items()))


# In[6]:
'''  Problem 12.2 Apply what you have learned to fill in the body of the function below, and add code for the tests indicated:'''

def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity

new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
print("original:", new_inventory)
new_inventory['strawberries'] == 10
add_fruit(new_inventory, 'strawberries', 25)
print("after adding strawberries:", new_inventory)
assert new_inventory['strawberries'] == 35


# In[7]:
'''  Problem 12.3 Write a program called alice_words.py that creates a text file named alice_words.txt containing an alphabetical listing of all the words, and the number of times each occurs, in the text version of Alice’s Adventures in Wonderland. (You can obtain a free plain text version of the book, along with many others, from http://www.gutenberg.org.) The first 10 lines of your output file should look something like this'''

import re
dict = {}

with open('alice.txt') as text:
    for line in text:
        line = line.strip().lower()
        line = re.sub(r'[0-9_]','', line)
        for word in line.split():
            if word.isalpha():
                if word in dict:
                    dict[word] += 1
                else:
                    dict[word] = 1             
text.close()

# top_ten = {k: dict[k] for k in sorted(dict.keys())[:10]}
# print(top_ten)
print("Alice appears in the text", dict['alice'], 'times')


# In[8]:
'''   Problem 12.4    What is the longest word in Alice in Wonderland? How many characters does it have?  '''
print("The longest word in Alice in Wonderland is:", sorted(dict.keys(), key=len)[-1])


# In[9]:
'''  Problem 12.5   Write a function named translator that takes a parameter containing a sentence in English (no punctuation and all words in lowercase) and returns that sentence translated to Pirate.  For example, the sentence “hello there students” should be translated to “avast there swabbies”.'''

pirate_dict = {"sir":"matey", "hotel":"fleabag inn", "student":"swabbie", "boy":"matey",
               "madam":"proud beauty","professor":"foul blaggart", "restaurant":"galley",
               "your":"yer", "excuse":"arr", "students":"swabbies", "are":"be", 
               "lawyer":"foul blaggart", "the":"th'", "restroom":"head", "my":"me", 
               "hello":"avast", "is": "be", "man":"matey"}

def pirate_translate(sentence):
    xlation = ""
    words = sentence.split()
    for w in words:
        if w in pirate_dict:
            word = pirate_dict[w] + " "
            xlation += word
        else:
            xlation += (w + " ")
    return xlation.strip()
            
test_txt = "hello there students"
test_out = "avast there swabbies"
print(test_txt, "translates to", pirate_translate(test_txt))
assert pirate_translate(test_txt) == test_out


# In[19]:
#Calculate average grade for each student

infile = open("studentdata.txt", "r")
aline = infile.readline().strip()    # aline reads one line and includes a \n at EOL that must be stripped
while aline:
    splitline=aline.split(" ")       # split the input string into fields
    student = splitline[0]           # the first field is the student's name
    scores = splitline[1:]           # the scores are in subsequent fields
    scores = [int(i) for i in scores]   # have to transform string scores into ints
    average = sum(scores)/len(scores)
    print(student, 'had an average score of', average)
    aline = infile.readline().strip()   # and read another line from the file

infile.close() 
