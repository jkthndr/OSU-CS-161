# Author: Oliver J. Smith
# Date: 2/23/21
# Description:

state_capitals = {
    "Washington": "Olympia",
    "Oregon": "Salem",
    "Idaho": "Boise",
    "Montana": "Helena"
}

# Exercises

# 1. Make a dictionary called "eng_to_span" where the keys are the English words "one" through "ten", and the
#       corresponding values are their Spanish translations.

eng_to_span = {
    "one": "uno",
    "two": "dos",
    "three": "tres",
    "four": "quatro",
    "five": "cinco",
    "six": "seis",
    "seven": "siete",
    "eight": "ocho",
    "nine": "nueve",
    "ten": "diez"
}

# 2. Using the dictionary from #1, write a loop that prints out both the key and value of each key-value pair, for
#       example the first iteration of the loop should print 'one' 'uno'.

# for n in eng_to_span:
#     print(n, eng_to_span[n])


# 3. Write a function name some_squares that takes a positive integer parameter and returns a dictionary where the
#       keys are the integers from 1 through the value of the parameter, and the corresponding values are the squares
#       of those integers.

# def some_squares(n):
#     d = {}
#     for i in range(1, n+1):
#         d[i] = i*i
#
#     return d

# Sets

# 1. Write a funciton called "unionize"

