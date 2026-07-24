# #------------------------------SETS---------------------------------
# pedofiles = {"Scouarnec"," Richard Huckle", "Peter Scully"}
# names = {"Peter Scully","Bob","Joe"}
# print(pedofiles.intersection(names))


# #------------------------------FUNCTIONS---------------------------------

# def value_added_tax(amount):
#     tax = amount * 0.25
#     total_amount = amount * 1.25
#     return f"{amount}, {tax}, {total_amount}"
    
# price = value_added_tax(100)    
# print(price, type(price))

# #------------------------------LOOPS---------------------------------
# print("1.*Loops are great*")
# print("2.**Loops are great**")
# print("3.***Loops are great***")
# print("4.****Loops are great****")
# print("5.*****Loops are great*****")

# i=0
# while 3 in range(5):
#     i += 1
#     print(f"{i}."+ "*"*i + "Loops are awesome" + "*"*i)
    

# friends = ['John','Terry','Eric','Michael','George']
# for index in range(len(friends)):
#     print(friends[index])

# print("For Loop done!")



is_raining = True
is_cold = False
print("Good Morning!")
if is_raining and is_cold: 
    print("Bring umbrella and jacket!")
elif is_raining and not(is_cold):
    print("Bring umbrella!")



# #------------------------------DICTIONARIES---------------------------------


# movie = {
#     'title' : 'Life of Brian',
#     'year' : 1979,
#     'cast' : ['John','Eric','Michael','George','Terry']
# }

# print(movie)
# test_list = movie[2]
# print(type(test_list))