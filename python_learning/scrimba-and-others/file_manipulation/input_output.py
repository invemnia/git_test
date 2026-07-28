black_man = open('random_text.txt','r')

# print(black_man.read(15))

# print(black_man.readline())
print("Read all lines: ", black_man.readlines())

print("Split lines: ", black_man.read().splitlines())

black_man.close()