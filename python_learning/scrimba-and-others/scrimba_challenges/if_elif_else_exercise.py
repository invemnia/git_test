print('if elif else - Exercise')


# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

first_num = int(input("First number: "))
second_num = int(input("Second number: "))
operation = input("Operation: ")


if (operation == "+") or (operation == "add"):
    print(first_num + second_num)
elif operation in ("-" or "minus"):
    print(first_num - second_num)
elif operation == ("/" or "divide"):
    print(first_num / second_num)
elif operation == ("*" or "times"):
    print(first_num * second_num)
else:
    print("Sorry that's all it can do")

print(operation == ("+" or "add"))



    

# ## making it with a function 
# def add(first,second):
#     addition = first + second
#     print(addition)

    