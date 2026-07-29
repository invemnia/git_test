# #------------------------------WORKSHEET-TESTING---------------------------------
# print("1." + str(round(2.3)))

# name = "Amy"
# print(f"|{name:_^11}|")


# print(365 // 4)
# print(91 * 4)




# #------------------------------PRE-LAB---------------------------------

###### Question 6


###### Question 10
##--attempt 1
# numbers = [12, 122, 3, 32, 14, 2, 400, 1, 42]
# new_numbers = []

# for i in numbers:
#     if i < 10:
#         numbers.remove(i)
# print(numbers)

#--atempt2: works but copies list
# numbers = [12, 122, 3, 32, 14, 2, 400, 1, 42]
# new_numbers = []

# def remove_10(numbers):
#     for i in numbers:
#         if i < 10:
#             new_numbers.append(i)
#     print(new_numbers)


#attempt3:
numbers = [12, 122, 3, 32, 14, 2, 400, 1, 42]

def remove_10(numbers):
    for i in numbers.copy():
        if i > 10:
            numbers.remove(i)
    return numbers
print(numbers)
print(remove_10(numbers))
    