# Author: Oliver J. Smith
# Date: 2/5/21
# Description:

# Exercises

# 1. Write a function call last_char that takes a string parameter and returns the last letter of that string

def last_char(s):
    """
    Return last letter of the string
    """

    return s[-1]

# 2. Write a function called midstring that takes a string parameter and returns a copy of that string minus its first
#       and last letters.

def midstring(s):
    """
    Return the string minus the first and last letters
    """

    return s[1:len(s)-1]

# 3. Write a function called sort_two_strings that takes two parameters and returns a single string of both of them
#       in dictionary order, ignoring case.

def sort_two_strings(s1, s2):
    """
    Sort two strings and return a single string in dictionary order
    """
    s1.upper()
    s2.upper()

    if s1.upper() < s2.upper():
        return str(s1)+" "+str(s2)

    return str(s2)+" "+str(s1)

# 4. Write a function called is_pal that takes a string parameter and returns True if that string is a palindrome.

def is_pal(s):
    """
    Determines if the given string is a palindrome; returns True or False.
    """
    if s == s[::-1]:
        return True
    return False

some_primes = [2,3,5,7,11,13,17,19,23,29,31]
some_names = ["Groucho","Harpo","Chico","Zeppo","Karl"]
some_stuff = [98,"Fido", -34.925, ["Phantom","Tollbooth"]]
one = ["juse me"]
zero = []

odds = [7,5,9,1,13,11,3]
evens = [8,4,10,6,2]
palindrones = ["hannah", "tacocat", "bob", "mom", "dad"]

# Next Set of Exercises

# 1. Write a function named every_other that takes as a parameter a list that only contains every other element
#       starting with the first one.

def every_other(s):
    """
     Take a list as a parameter and return every other element
    """
    return s[::2]

# 2. Write a function name array_sum that takes a parameter list and returns the total number of characters in all
#       strings.

def array_sum(s):
    """
    Take a list as a parameter and return the total number of characters in all strings
    """
    count = 0
    for word in s:
        for ch in s:
            count += 1
    return count

def rev_string_list(sl):
    return [s[::-1] for s in sl]