# #------------------------------SETS---------------------------------
# pedofiles = {"Scouarnec"," Richard Huckle", "Peter Scully"}
# names = {"Peter Scully","Bob","Joe"}
# print(pedofiles.intersection(names))


# ------------------------------LISTS----------------------------

# people = ["Peter Scully","Bob","Joe","Joe", "Richard Huckle"]
# people.append("Mark")
# people[-1] = ("Actual Mark")

# people.insert(0, "The Got")
# people[0] = "The Goat" #my bad
# print(people)
# print('--------')
# print(people.index("Joe"))
# print(people.count('Joe'))
# print('--------')
# people.remove("Joe") #one joe gone
# print(people)
# print('--------')


# print(people.pop(-3))
# print(people)


# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# more_friends = ['Joe', 'Videsh']
# friends_list = ['Eric','John','Michael','Terry','Graham']

# # print(csv.split(","))

# long_string = '-nigga-'.join(friends_list + more_friends)
# print(long_string)
# print(type(long_string))
# print('\n')

# print(long_string.split('-nigga-'))


# #------------------------------FUNCTIONS---------------------------------

# def value_added_tax(amount):
#     tax = amount * 0.25
#     total_amount = amount * 1.25
#     return f"{amount}, {tax}, {total_amount}"
    
# price = value_added_tax(100)    
# print(price, type(price))



# def hello(name="nigga"):
#     print("hello",name)
    

# username = input("> ")
# hello(username)

# for i in range(3):
#     hello(username)

# def area(length, width):
#     print(str(length * width) + " square feet")


# def main():
#     other_area = area(10,10)
#     area(50, 20)


# main()



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

# # print("For Loop done!")


# is_raining = True
# is_cold = False
# print("Good Morning!")
# if is_raining and is_cold: 
#     print("Bring umbrella and jacket!")
# elif is_raining and not(is_cold):
#     print("Bring umbrella!")



# #------------------------------DICTIONARIES---------------------------------

#Calcutating marks for the lab01 to see if I have to do questions 19-25



# movie = {
#     'title' : 'Life of Brian',
#     'year' : 1979,
#     'cast' : ['John','Eric','Michael','George','Terry']
# }

# print(movie)
# test_list = movie[2]
# print(type(test_list))

# characters = {'Walter': 'Broken', 
#              'Palpatine': 'Evil', 
#              'Madara': 'Broken', 
#              'Goku': 'Good'
# }


# for character in characters:
#     print(character, characters[character], sep="->")


# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]




# for student in students:
#     print(student['name'], student['house'], sep="__")

# print(students[3]["name"])

# #------------------------LIST COMPREHENSION---------------------


# new_list = []
# for num in range(5):
#     new_list.append(num*num)
# print(new_list)

# comp_list = [num*num for num in range(5) if num[4] == 16]
# print(comp_list)

# #------------------------BASICS-NO-THEME---------------------
# marks = (10 * 0.1) + (0.5 * 4) + (4 * 1) 
# print(float(marks))

            # making a function for even or odd

# def iseven(n):
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print('odd')

# iseven(12341234)

#without printing in function

def main():
    number = int(input('Number: '))
    if iseven(number):
        print("Even")
    else: 
        print("odd")

def iseven(n):
    return True if n % n == 0 else False

    #orrr
    # if n % 2 == 0:
    #     return True
    # else:   
    #     return False

main()