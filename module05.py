# Author: Oliver J. Smith
# Date: 2/1/21
# Description:

# Exploration: Recursion

def factorial(num):
    """
    returns the factorial of num
    """
    if num == 0:
        return 1

    return num * factorial(num-1)

def gcd(a, b):
    """
    Returns the greatest common divisor of a and b
    """
    if a % b == 0:
        return b

def hailstone(num):
    """
    Returns the numer of steps it takes for a hailestone sequence that starts at num to reach 1
    """
    if num == 1:
        return 0
    if num % 2 == 0: # if num is even
        return hailstone(num/2) + 1
    else:
        return hailstone(num*3+1) + 1

# Exercises


# 1. Write a recursion function called countdown - unfinished

def countdown(num):
    """
    Take a positive integer and return a string that counts down from that number to 1

    Sample input: 5
    Expected output: "5, 4, 3, 2, 1"
    """
    # print(num)

    if num < 2:
        return str(num)
    return str(num)+" "+countdown(num-1)


# 2. Exercise 2 - unfinished

def countup(num):
    """
    Take a positive integer and return a string that counts down from that number to 1

    Sample input: 5
    Expected output: "1, 2, 3, 4, 5"
    """
    if num < 2:
        return str(num)
    return countup(num-1)+" "+str(num)

# 3. Exercise 3

def sum_countup(n):
    if n == 1:
        return 1
    return n + sum_countup(n-1)

class Rectangle:
    """
    Represents a two-dimensional rectange with methods to calculate its volume and surface area.
    """

    def __init__(self, width, height):
        """ Creates a Rectangle object with the specified width and height."""
        self.width = width
        self.height = height

    def area(self):
        """"Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2*self.width + 2*self.height

class HourlyWorker:
    """
    Description
    """

    def __init__(self,_name, _ID, _wage):
        self._name = _name
        self._ID = _ID
        self._wage = _wage

class Box:
    """
    Description
    """

    def __init__(self, _length, _width, _height):
        """ Description"""
        self._length = _length
        self._width = _width
        self._height = _height

    def volume(self):
        """Description"""

        return self._length * self._width * self._height

    def surface_area(self):
        """Description"""

        return 2 * ((self._width * self._height) + (self._length * self._width) + (self._length * self._height))