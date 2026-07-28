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
# #first attempt:
# numbers = [-3, 8, 68, 10, 14, -9, 3, -17, -7, 14, 1, -1, -12, -6, 32]


# def update_negative(any_list):
#     for num in range(len(any_list)):
#         if any_list[num] < 0:
#             negative = any_list[num]-1
#             any_list[num] = (negative)
    
    
# update_negative(numbers)
# print(numbers)

##------------------------------Q-15---------------------------------##
# words_list = ['lamp', 'window', 'window', 'city', 'bush', 'window', 'floor', 'flower', 'chair']

# for word in words_list.copy():
#     if len(word) == 5:
#         words_list.remove(word)
# print(words_list)

# # #adding funciton:


# def remove_words_length_5(list_of_words):
#     for word in list_of_words.copy():
#         if len(word) == 5:
#             list_of_words.remove(word)
# remove_words_length_5(words_list)
# print(words_list)

##------------------------------Q-16---------------------------------##    
# Do the following 16-23 for sunday




##------------------------------Q-19-FIXING---------------------------------##   

def display_country_gdp(countries_gdp, column_width=19):
    
    print(f"{'Country':>{column_width}} GDP (Billion $)\n{'-' * (column_width + (len(countries_gdp)))}")
    
    for country, gdp in countries_gdp.items():
        print(f"{country:>{column_width}} {gdp}")
def display_country_gdp(countries_gdp, column_width=19):
    print(f"{'Country':>{column_width}} GDP (Billion $)}")
    for country, gdp in countries_gdp.items():
        print(f"{country:>{column_width}} {gdp}")



def display_country_gdp(countries_gdp, column_width=19):
    header = f"{'Country':>{column_width}} GDP (Billion $)"
    print(header)
    print("-" * len(header))

    for country, gdp in countries_gdp.items():
        print(f"{country:>{column_width}} {gdp}")


####Actual Answer###
def display_country_gdp(countries_gdp, column_width=19):
    header = f"{'Country':>{column_width}} GDP (Billion $)"
    print(header)
    print(f"-" * (len(header) + 1))
    for country, gdp in countries_gdp.items():
        print(f"{country:>{column_width}} {gdp}")





##------------------------------Q-17---------------------------------##    
#Just testing out the cards#



# alph = "abcdefghijklmnopqrstuvwxyz"

# result = {}

# for char in "cab":
#     result[char] = alph.index(char) + 1 #checks position against the alphabet

 