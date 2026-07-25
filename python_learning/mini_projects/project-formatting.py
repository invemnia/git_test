
def main():
    username = input("what's your name: ")
    hello(username)



#reads defs first then goes to main
def hello(someone):
    print('Hello,', someone.title())


main()