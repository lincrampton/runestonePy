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
'''  Problem 9.2 In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. Output these names in order.'''

prefixes = ['J', 'K', 'L', 'M', 'N', 'Ou', 'P', 'Qu' ]
suffix = "ack"

for p in prefixes:
    print(p + suffix)
    
print(' '.join([str(lst)+suffix for lst in prefixes]))


# In[3]:
''' Problem 9.6   Write a function that reverses its string argument.'''
def reverse(astring):
    return astring[::-1]
print("iamsam", reverse('iamsam'))


# In[4]:
'''  Problem 9.7 Write a function that mirrors its string argument, generating a string containing the original string and the string backwards.'''
def mirror(mystr):
    return mystr+mystr[::-1]
print(mirror('iamsam'))


# In[5]:
''' Problem 9.6 Write a function that removes all occurrences of a given letter from a string.'''
def remove_letter(theLetter, theString):
    return theString.replace(theLetter,'')
def remove_first_letter(theLetter, theString):
    return theString.replace(theLetter,'',1)

test_string = 'iamsamiami'
print("Original String:\t",test_string)
print("Remove First:\t\t", remove_first_letter('i', test_string))
print("Remove All:\t\t", remove_letter('i', test_string))


# In[6]:
''' Problem 9.9 Write a function that recognizes palindromes.  (Hint: use your reverse function to make this easy!).'''
def is_palindrome(myStr):
    return myStr == myStr[::-1]
print("iamsamiam is a palindrome?", is_palindrome('iamsamiam'))
print('samimas is a palindrome?', is_palindrome('samimas'))


# In[7]:
''' Problem 9.10 Write a function that counts how many non-overlapping occurences
of a substring appear in a string.'''

import re
def count_in_string(substr, theStr):
    return len(re.findall(substr, theStr))

'''If I can't use re library, then make a locus in the string and check if the string startswith the substring, then move locus'''
import string
def count(substr, theStr):
    occurs, locus = 0,0  
    while locus < len(theStr) - len(substr) + 1:
        if theStr[locus:].startswith(substr):
            occurs += 1
            locus += len(substr)
        else:
            locus += 1
    return occurs

test_theStr='banana'
test_substr='an'
print(test_substr,'shows up', count_in_string(test_substr, test_theStr), 'times in', test_theStr)
print(test_substr,'shows up', count(test_substr, test_theStr), 'times in', test_theStr)

test_theStr='Mississippi'
test_substr='is'
print(test_substr,'shows up', count_in_string(test_substr, test_theStr), 'times in', test_theStr)
print(test_substr,'shows up', count(test_substr, test_theStr), 'times in', test_theStr)

test_theStr='aaaaaa'
test_substr='aaa'
print(test_substr,'shows up', count_in_string(test_substr, test_theStr), 'times in', test_theStr)
print(test_substr,'shows up', count(test_substr, test_theStr), 'times in', test_theStr)

test_theStr='banana'
test_substr='nanan'
print(test_substr,'shows up', count_in_string(test_substr, test_theStr), 'times in', test_theStr)
print(test_substr,'shows up', count(test_substr, test_theStr), 'times in', test_theStr)


# In[8]:
''' Problem 9.11 Write a function that removes the first occurrence of a string from another string.'''
def remove(substr,theStr):
    return theStr.replace(substr,"",1)

'''Write a function that removes all occurrences of a string from another string.'''
def remove(substr,theStr):
    return theStr.replace(substr,"")


# In[9]:
'''   Problem 9.18   Write a function that implements a substitution cipher.  In a substitution cipher one letter is substituted for another to garble the message.  For example A -> Q, B -> T, C -> G etc. your function should take two parameters, the message you want to encrypt, and a string that represents the mapping of the 26 letters in the alphabet.  Your function should return a string that is the encrypted version of the message.'''
import random

def makeCipherDict(alphabet):
    alephbet = list(alphabet)
    alphabet = list(alphabet)
    random.shuffle(alephbet)
    return dict(zip(alphabet, alephbet))

def makeReverseCipherDict(cipher_dict):
    return {value: key for key, value in cipher_dict.items()}

def encrypt(input_text, working_dict):
    return ''.join(working_dict.get(c) for c in input_text)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
cipher_dict = makeCipherDict(alphabet)  # alephbet is mapping of original letters to randomized letters
reverse_dict = makeReverseCipherDict(cipher_dict)

original_text='IamSamIam'
encrypted_text = encrypt(original_text, cipher_dict)
decrypted_text = encrypt(encrypted_text, reverse_dict)
print(original_text, "is the original text")
print(encrypted_text, "is the encrypted text")
print(decrypted_text, "is the decrypted text")

test_text_string ='dlfdskjfdsjfdjlfjldllfdjIII'

# encrypting with cipher_dict and then encrypting with the reverse_dict returns original string
assert  encrypt(encrypt(test_text_string, cipher_dict), reverse_dict) == test_text_string


# In[10]:
''' Problem 9.19 Write a function called remove_dups that takes a string and creates a new string by only adding those characters that are not already present.  In other words, there will never be a duplicate letter added to the new string''' 
def remove_dups(astring):
    return ''.join(set(astring))

from collections import OrderedDict
def remove_dups_ordered(astring):
    return "".join(OrderedDict.fromkeys(astring)) 

    
print(remove_dups("mississippi"))   #should print the letters misp in some order
print(remove_dups_ordered("mississippi"))   #should print misp
    
assert ''.join(sorted(remove_dups("mississippi"))) == 'imps'
assert remove_dups_ordered("mississippi") == 'misp'


# In[11]:
''' Problem 9.21 Write a function called rot13 that uses the Caesar cipher to encrypt a message.  The Caesar cipher works like a substitution cipher but each character is replaced by the character 13 characters to ‘its right’ in the alphabet. So for example the letter a becomes the letter n. If a letter is past the middle of the alphabet then the counting wraps around to the letter a again, so n becomes a, o becomes b, etc.  Hint: think modulo arithmetic.'''

def rot13v1(original_text):
    ord_a = ord('a')
    offset = 13 # function is rot13
    return_str=''
    for c in original_text.lower():
        if c.isalpha():
            return_str += chr(  ( (ord(c)-ord_a + offset) % 26 ) + ord_a )
        else:
            return_str += c
    return return_str


def rot13v2(original_text):
    import codecs
    return codecs.encode(original_text, 'rot_13')

assert rot13v1('abcde') == rot13v2('abcde')
assert rot13v1('nopqr') == rot13v2('nopqr')
print(rot13v1(rot13v1('Since rot13v1 is symmetric you should see this message')))
print(rot13v2(rot13v2('Since rot13 is symmetric you should see this message')))


# In[12]:
'''   Problem 9.22 Modify this code so it prints each subtotal, the total cost, and average price to exactly two decimal places. '''

def checkout():
    total, count = 0, 0
    Finished = False
    while not Finished:
        price = int(input('Enter price of item (0 when done): '))
        if price:
            count += 1
            total += price
            print('Subtotal: ${:0.2f}'.format(total))
        else:
            Finished = True
    if count:  
        average = float(total)/ count
    else:
        average = 0
    print('Total items:', count)
    print('Total ${:0.2f}'.format(total))
    print('Average price per item: ${:0.2f}'.format(average))

checkout()


# In[13]:
''' Problem 10.2 Create a list called myList with the following six items: 76, 92.3, “hello”, True, 4, 76.  Begin with the empty list shown below, and add 6 statements to add each item, one per item.  The first three statements should use the append method to append the item to the list, and the last three statements should use concatenation.'''

myList = []

#myList.append(76)
#myList.append(92.3)
#myList.append('hello')
myList.extend((76, 92.3, 'hello'))     # can do this instead of line by line appending
otherlist = [True, 4, 76]
myList += otherlist
print(myList)


# In[14]:
''' Problem 10.3 Starting with the list of the previous exercise, write Python statements to do the following: Append “apple” and 76 to the list; Insert the value “cat” at position 3.; Insert the value 99 at the start of the list. Find the index of “hello”.Count the number of 76s in the list.  Remove the first occurrence of 76 from the list.  Remove True from the list using pop and index.'''

myList = [76, 92.3, 'hello', True, 4, 76]
myList +=  (('apple', 76))
myList[3:3] = 'cat'
myList[0:0] = [99]
hello_index = myList.index('hello')
count_o_76 = myList.count(76)
myList.remove(76)
myList.pop(myList.index(True)) # g

print('hello index', hello_index, '\ncount of 76 in list', count_o_76, "\n", myList)


# In[15]:
'''  Problem 10.4
Write a function called average that takes a list of numbers
as a parameter and returns the average of the numbers'''
def average(numlist):
    return sum(numlist)/len(numlist)

assert average([47,48,49,50,51]) == 49
print(average([10,12,6,12]))


# In[16]:
'''  Problem 10.5 
Write a Python function named max that takes a parameter containing 
a nonempty list of integers and returns the maximum value. 
There is a builtin function named max but pretend you cannot use it.'''

def max(lst):
    lst.sort(reverse=True)
    return lst[0]

sam=[10,12,6,12]
assert max(sam) == 12
print('max of sam should equal 12 and does equal', max(sam))


# In[17]:
'''  Problem 10.6 Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs.  For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:'''
def sum_of_squares(xs):
    return sum(x**2 for x in xs)

xs = [4,5,3,2,1]
assert sum_of_squares(xs) == 55
print('Sum of squares of', xs, 'should equal 55 and does equal', sum_of_squares(xs))


# In[18]:
'''  Problem 10.7 Write a function to count how many odd numbers are in a list.'''
def countOdd(lst):
    return len([x for x in lst if x%2])

assert countOdd([7,6,5,4,3,2,1]) == 4


# In[19]:
'''  Problem 10.8  Sum up all the even numbers in a list.'''
def sumEven(lst):
    return sum(num for num in lst if not num%2)

assert sumEven([11,2,4,13,127, -6, 22]) == 22


# In[20]:
'''  Problem 10.9 Sum up all the negative numbers in a list.'''
def sumNegatives(lst):
    return sum(s for s in lst if s<0)

assert sumNegatives([-5,4,3,2,-1]) == -6


# In[21]:
''' Problem 10.10 Count how many words in a list have length 5.'''
def countWords(data):
    return sum(1 for i in data if len(i) == 5)

assert countWords(['a','b','ccccc']) == 1
assert countWords(['a','aaaab','ccccc']) == 2


# In[22]:
'''  Problem 10.11 Sum all the elements in a list up to but not including the first even number.'''
def sumUntilEven(lst):
    oddSum=0
    for l in lst:
        if l%2:
            oddSum += l
        else:
            break
    return oddSum

test_case = [3,5,7,8,12,14,22]
assert sumUntilEven(test_case) == 15
print('running sumUntilEven on', test_case, 'should return 15 and does return', sumUntilEven(test_case))


# In[23]:
'''  Problem 10.12 Count how many words occur in a list up to and including the first occurrence of the word “sam”.''' 
def count(lst):
    pre_sam = 0
    
    for l in lst:
        if l=='sam':
            pre_sam += 1
            break
        else:
            pre_sam += 1
    return pre_sam

test_case = [1,3,4,'sam',2,'bob']
assert count(test_case) == 4
print('Running this count function on', test_case, 'should return 4 and does return',count(test_case))


# In[24]:
'''  Problem 10.14 Write a function replace(s, old, new) that replaces all occurences of old with new in a string s: Hint:  Use split and join'''

def replace(whole_string, old_sub, new_sub):
    return new_sub.join(whole_string.split(old_sub))
    
assert replace('Mississippi', 'i', 'I') == 'MIssIssIppI'


s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
assert replace(s, 'om', 'am') == 'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!'

assert replace(s, 'o', 'a') == 'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!'


# In[25]:
'''  Problem 10.17 Create a list named randlist containing 100 random integers between 0 and 1000 Use iteration, append, and the random module).'''
import random
([random.randint(1,1001) for x in range(100)])

assert len(([random.randint(1,1001) for x in range(100)])) == 100


# In[26]:
'''  Problem 7.10.14 Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.  '''
def is_even(n):
#     return bool(not(n%2))
    return False if n%2 else True

for _ in [ -14, -7, 0, 5, 11, 12, 14]:
    print("is_even", _, "returns", is_even(_))


# In[9]:
def rev_string_via_list(orig_string):
    reversed = []
    for c in orig_string:
        reversed.insert(0,c)
    return ''.join(reversed)

test_string = 'Green Eggs and Ham'
print(test_string)
print(rev_string_via_list(test_string))
print(rev_string_via_list(rev_string_via_list(test_string)))   # should be the original string


# In[18]:
# STRINGS ARE IMMUTABLE
s = 'abc12321cba'
print(s, s.replace('a', ''))
s.replace('a','b')
print(s)

