# Author: Oliver J. Smith
# Date: 2/12/21
# Description:

# def square_val(val):
#     val[0] = val[0] * val[0]
#     print(val)
#
# # Exercises
#
# # 2. Write a function named insert_front that takes a parameter as a list and adds that value to the front.
# #       >>> insert_front([9, -55, 37],["bob"])
# #           Sample input: [9, -55, 37]
# #           Sample input: insert_front(["Bob"])
# #           Expected output: ["Bob", 9, -55, 37]
#
# def insert_front(a_list, new_el):
#     """
#     Return the list with the new value added to the beginning of the list
#     """
#     a_list[0:0] = [new_el]
#     return a_list
#
# def delete_last(some_list):
#     """
#     Define
#     """
#     del some_list[-1]
#     return some_list

def even_numbers_only(mixed_list):
    for index in range(len(mixed_list)):
        if mixed_list[index] % 2 != 0:
            mixed_list[index] = mixed_list[index] * 2

    return mixed_list

num_list = [7, 2, 3, 1, 8]
even_numbers_only(num_list)
print(num_list)