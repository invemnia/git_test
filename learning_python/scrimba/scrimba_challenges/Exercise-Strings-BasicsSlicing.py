msg='welcome to Python 101: Strings'
  
# testing different ways of doing it. Commas = tuple, " " equal string
# test_msg = msg[18].title(),msg[0:7].title(), msg[-5:-1].title(), msg[8:10].title(),(msg[-17:-19:-1] + msg[2:0:-1] + msg[-5]).title()

# This is a method with title attached to everything
longAss_method = msg[18].title() + " " + msg[0:7].title() + " " + msg[-5:-1].title() + " " + msg[8:10].title() + " " + (msg[-17:-19:-1] + msg[2:0:-1] + msg[-5]).title()

new_msg = msg[18] + " " + msg[0:7] + " " + msg[-5:-1] + " " + msg[8:10] + " " + (msg[-17:-19:-1] + msg[2:0:-1] + msg[-5])

print(new_msg.title())
print(new_msg.title()[::-1])