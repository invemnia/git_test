#-__-_______-------_______-----__Claude learning_--__---------__-___--___-___---_--_
# def say_bye():
#     print("bye")

# say_bye()


#### experimenting with claude answers

#q9
def read_file(filename):
    result = []
    file = open(filename, "r")
    for line in file:
        result.append(line.strip())   # .strip() removes the \n at the end
    file.close()
    return result