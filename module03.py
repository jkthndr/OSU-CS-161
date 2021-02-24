# Author: Oliver J. Smith
# Date: 1/14/21
# Description: Module 3

# Exploration: Comparision operators and logical operators


# 1. Print the value of 17 < 5

# exercise1_value = 17 < 5
# print(exercise1_value)

# 2. Write code that reads a number from the user, assigns it a variable, and then prints True if that value is greater than 10, but prints false

# print("Enter in a value and determine if it's greater than 10\n")
# user_value = input()
# print(int(user_value) > 10)

# 3. Write code that reads a number from the user, assignts it to a variable, and then prints True if that value is between 50 and 100 (inclusive), but prints False otherwise.

# print("Enter in a value and determine if it's greater than 10\n")
# user_value = input()
# print(50 < int(user_value) < 100)

# Exploration: Conditional execution

# num = int(input())
# if num % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

# score = int(input("Enter a score: "))
# if score >= 90:
#     grade = "A"
# else:
#     if score >= 80:
#         grade = "B"
#     else:
#         if score >= 70:
#             grade = "C"
#         else:
#             if score >= 60:
#                 grade = "D"
#             else:
#                 grade = "F"
# print("Letter grade = ", grade)

# Exercises

# 1. Write code that reads a number from the user, assigns it to a variable, and then prints "in range" if that value is between 50 and 100
# but prints "out of range" otherwise.

# user_range = int(input("Choose a number: "))
# if 50 < user_range < 100:
#     print("In range")
# else: print("Out of range")

# 2. Write code that reads a number from the user, assigns it to a variable, and then prints "small" if it's less than 10, prints "medium" if it's
# at least 10 but less than 50, and prints "large" if it's at least 50

# user_size = int(input("Enter your size: "))
# if user_size < 10:
#     print("Small")
# elif 10 <= user_size <=50:
#     print("Medium")
# elif user_size >=50:
#     print("Large")

# 3. Write code that reads an integer from the user and assigns it to a variable. If that integer is a value from 1-5, your
# program should print out the English word for that number. Otherwise it should print "intput not recognized".

# user_number = int(input("Choose a number between 1 and 4: "))
# if user_number == 1:
#     print("One")
# elif user_number == 2:
#     print("Two")
# elif user_number == 3:
#     print("Three")
# elif user_number == 4:
#     print("Four")

# Accumulates total score until it's 100 or greater

# total_score = 0
# while total_score < 100:
#     total_score += int(input("Enter your score for this round: "))
#     print("total so far -", total_score)

# word = "University"
# for letter in word:
#     print(letter)

# for num in range(100,1,-2):
#     if num == 50:
#         print("*",num,"*")
#     else: print(num)

# A nested for loop

# total_num_letters = 0
# print("Please enter the names of your three favorite animals.")
# for val in range(1,4):
#     animal = input()
#     for letter in animal:
#         total_num_letters += 1
# print("Those names contained a total of", total_num_letters, "characters.")

# Exercises

# 1. Write code that reads an integer from the user and prints out the sum of the integers
# from 1 to that number.

# user_number = int(input("Provide me with a number:\n"))
# for val in range(1, (user_number+1)):
#     user_number += 1
# print(user_number)

# 2. Write code that reads a string from the user, counts how many characters are in the string,
# and prints out "odd" if that number is odd, but prints "even" if that number is even.

# total_num_letters = 0
#
# user_string = input()
# for letter in user_string:
#     total_num_letters += 1
# if total_num_letters % 2 == 0:
#     print("even")
# else: print("odd")

# 3. Write code that continues reading a string from the user and printing it out until the user enters "quit">

# "Pessimism = sin against science."
# "Energy out of the tin, climate control, perpetual growth!"
# "To convert Iceland into a tropical paradise - "
# "no problem. The rest makes no difference."

# user_input = input()
# while user_input != "quit":
#     print(user_input)
#     user_input = input()

name = "Gianni Suet Man Law-Smith + Oliver Jacob Smith"
fn = ""
for letter in name:
    # if letter == "Z":
    #     continue
    fn += letter
    print(fn)