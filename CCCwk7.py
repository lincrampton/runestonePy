#!/usr/bin/env python
# coding: utf-8

# ## Homework Week 7
# 
# Lin Crampton, CCC CIS157, Stefan Bund

# In[1]:
'''  Problem 17.11.15 Given three points that fall on the circumference of a circle, find the center and radius of the circle.'''

from sympy.geometry import *
def find_center_from_points(point1, point2, point3):
    circ = Circle(point1, point2, point3)
    return circ.center

def find_radius_from_points(point1, point2, point3):
    circ = Circle(point1, point2, point3)
    return circ.radius

p1 = Point(1, 2)
p2 = Point(-1, 4)
p3 = Point(3, -1)

print('The center of the circle is', find_center_from_points(p1,p2,p3)[1])
print('The radius of the circle is', find_radius_from_points(p1,p2,p3))


# In[2]:
'''   Problem 18.6.2 We can represent a rectangle by knowing three things: the location of its lower left corner, its width, and its height.  Create a class definition for a Rectangle class using this idea.  To create a Rectangle object at location (4,5) with width 6 and height 5, we would do the following r = Rectangle(Point(4, 5), 6, 5)
'''
class Rectangle:
    # Create a new rectange at the given location, with given height+width
    def __init__(self, initLocation, initWidth, initHeight):
        self.location = initLocation
        self.width = initWidth
        self.height = initHeight
    
    def __str__(self):
        return "location:"  + str(self.location) + ", height=" + str(self.height) + ", width =" + str(self.width)


P1 = Point(4,5)
H1 = 5
W1 = 6

linz_rect = Rectangle(P1, W1, H1)
print(linz_rect)


# In[3]:
'''  Problem 18.6.5 Add the following accessor methods to the Rectangle class: getWidth, getHeight, __str__..'''

class Rectangle: 
    # Create a new rectange at the given location, with given height+width
    def __init__(self, initLocation, initWidth, initHeight):
        self.location = initLocation
        self.width = initWidth
        self.height = initHeight
            
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width
    
    def getLocation(self):
        return self.location
    
    def __str__(self):
        return "location:"  + str(self.location) + ", height=" + str(self.height) + ", width =" + str(self.width)

test_point = Point(4,5)
test_height = 5
test_width = 6

linz_rect = Rectangle(test_point, test_height, test_width)
print(linz_rect)


# In[4]:
'''  Problem 18.6.7 Add a method area to the Rectangle class that returns the area of any instance'''
class Rectangle: 
    # Create a new rectange at the given location, with given height+width
    def __init__(self, initLocation, initWidth, initHeight):
        self.location = initLocation
        self.width = initWidth
        self.height = initHeight
            
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width
    
    def getLocation(self):
        return self.location
    
    def transpose(self):
        self.height, self.width = self.width, self.height
        
    def area(self):
        return self.height * self.width
        
    def __str__(self):
        return "location:"  + str(self.location) + ", height:" + str(self.height) + ",width:" + str(self.width)

test_point = Point(4,5)
test_height = 5
test_width = 6

linz_rect = Rectangle(test_point, test_height, test_width)
# print(linz_rect)

r = Rectangle(Point(0, 0), 10, 5)
assert r.area() == 50
assert linz_rect.area() == 30


# In[5]:
'''  Problem 18.6.10 Write a perimeter method in the Rectangle class so that we can find the perimeter of any rectangle instance:'''

class Rectangle: 
    # Create a new rectange at the given location, with given height+width
    def __init__(self, initLocation, initWidth, initHeight):
        self.location = initLocation
        self.width = initWidth
        self.height = initHeight
            
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width
    
    def getLocation(self):
        return self.location
    
    def transpose(self):
        self.height, self.width = self.width, self.height
        
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)
        
    def __str__(self):
        return "location:"  + str(self.location) + ", height:" + str(self.height) + ",width:" + str(self.width)

test_point = Point(4,5)
test_height = 5
test_width = 6

linz_rect = Rectangle(test_point, test_height, test_width)
# print(linz_rect)

r = Rectangle(Point(0, 0), 10, 5)
assert r.area() == 50
assert linz_rect.area() == 30

r = Rectangle(Point(0, 0), 10, 5)
assert r.perimeter() == 30
assert linz_rect.perimeter() == 22
print(linz_rect.perimeter(), 'is the perimeter of a rectangle with height', linz_rect.height, 'and width of', linz_rect.width)


# In[6]:
'''   Problem 18.6.12
Write a transpose method in the Rectangle class that swaps the width and the height
of any rectangle instance:'''
'''  Problem 18.6.5
Add the following accessor methods to the Rectangle class: 
getWidth, getHeight, __str__..'''

class Rectangle: 
    # Create a new rectange at the given location, with given height+width
    def __init__(self, initLocation, initWidth, initHeight):
        self.location = initLocation
        self.width = initWidth
        self.height = initHeight
            
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width
    
    def getLocation(self):
        return self.location
    
    def transpose(self):
        self.height, self.width = self.width, self.height
        
    def __str__(self):
        return "location:"  + str(self.location) + ", height:" + str(self.height) + ",width:" + str(self.width)

test_point = Point(4,5)
test_height = 5
test_width = 6

r = Rectangle(Point(100, 50), 10, 5)
print("The original width and height of the rectangle are:", r.width, 'and', r.height)
r.transpose()
print("The transposed width and height of the rectangle are:", r.width, 'and', r.height,'\n')


print("The original width and height of linz_rect are:", linz_rect.width,'and', linz_rect.height)
linz_rect.transpose()
print("The transposed width and height of linz_rect are:", linz_rect.width, 'and', linz_rect.height)


# In[7]:
'''   Problem 18.6.17 Write a new method called diagonal that will return the length of the diagonal that runs from the lower left corner to the opposite corner.'''

class Rectangle: 
    # Create a new rectange at the given location, with given height+width
    def __init__(self, initLocation, initWidth, initHeight):
        self.location = initLocation
        self.width = initWidth
        self.height = initHeight
            
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width
    
    def getLocation(self):
        return self.location
        
    def diagonal(self):
        return (self.width**2 + self.height**2)**(0.5)
        
    def __str__(self):
        return "location:"  + str(self.location) + ", height:" + str(self.height) + ",width:" + str(self.width)

r = Rectangle(Point(100, 50), 12, 5)
print(r.diagonal(), 'is the hypoteneuse of a rectangle with width', r.width, 'and height', r.height)
