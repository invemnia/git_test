#-__-_______-------_______-----__Claude learning_--__---------__-___--___-___---_--_
def say_bye():
    print("bye")

say_bye














#----------------------------Q-8-------------------------------#
# ---attempt1: 

# def get_valid_integer(prompt, min_value, max_value):
#     while True:
#         value = int(input(prompt))
#         if (min_value < value < max_value) or (max_value > value > min_value):
#             return value
#             break   
            

    
# number = get_valid_integer("Enter an integer: ", 1, 5)
# print(number)


# # --Atempt 2: (works). Removed break and made it inclusive
# def get_valid_integer(prompt, min_value, max_value):
    
#     while True:
#         value = int(input(prompt))
#         if (min_value <= value <= max_value) or (max_value >= value >= min_value):
#             return value
            

    
# number = get_valid_integer("Enter an integer: ", 1, 5)
# print(number)


#making it better 
def get_valid_integer(prompt, min_value, max_value):
    
    while True:
        value = int(input(prompt))
        if min_value <= value <= max_value:
            return value
            

    
number = get_valid_integer("Enter an integer: ", 1, 5)
print(number)

#     #----------------------------Q-12-------------------------------#
# a_dict = {'Kaitaia': [233.8, 199.6, 200.0, 163.9, 146.5, 127.4, 139.5, 161.3, 169.7, 194.7, 193.7, 202.2], 
# 'Auckland': [240.3, 203.4, 200.8, 169.3, 149.1, 126.1, 133.9, 153.7, 159.0, 180.5, 203.8, 201.9], 
# 'Tauranga': [269.0, 221.5, 221.4, 184.3, 170.9, 134.1, 149.9, 176.4, 178.2, 214.8, 240.0, 241.0]}

# def print_data(sunshine_dict):
#     for locations in sunshine_dict.keys():
#         print(locations)
#         for values in sunshine_dict.values():
#             print(values)

# print_data(a_dict)

