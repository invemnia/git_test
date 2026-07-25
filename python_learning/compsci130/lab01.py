##------------------------------LAB-QUESTIONS---------------------------------##

##------------------------------Q-11---------------------------------##


##answer without function

# first, last = input("Enter your full name: ").title().split()                
# print(f'*****\n{first[0]}. {last[0]}.\n*****')

##answer with function

# def get_intials(user_input):
#     first_name, last_name = user_input.title().split()
#     first_inital = first_name[0]
#     last_inital = last_name[0]
#     print(f'*****\n{first_inital}. {last_inital}.\n*****')
    

# get_intials(input("Enter in your full name: "))

##from claude: (basically my previous one but smaller)

# def print_initials(full_name):
#     first, last = full_name.title().split()
#     print(f'*****\n{first[0]}. {last[0]}.\n*****')

# print_initials(input("Enter your full name: "))

##------------------------------Q-12---------------------------------##

##first attempt:
# usernumber = int(input('Enter a number of centimetres: '))
# m = usernumber // 100
# cm_left = usernumber % 100

# if m == 1:
#     print(f'That is {m} metre and {cm_left} centimetres.')
# else:
#     print(f'That is {m} metres and {cm_left} centimetres.')


#second attempt: trying to make it so I don't repeat myself twice with both prints
# usernumber = int(input('Enter a number of centimetres: '))
# m = usernumber // 100
# cm_left = usernumber % 100

# print(f'That is {m} metre{'s'} and {cm_left} centimetres.')

##------------------------------Q-13--------------------------------##

##irst attempt:

# import math 
# radius = int(input('Enter the radius: ')) 
# diameter = 2 * radius
# quarter_circle = (1/4) * (math.pi) * (radius**2)
# print(f'Diameter: {math.ceil(diameter)}\nArea of the quarter circle: {math.ceil(quarter_circle)}')
 

##------------------------------Q-14---------------------------------##
numbers = [1, 2, 3]


for n in numbers:
    n = n * 10

print(numbers)