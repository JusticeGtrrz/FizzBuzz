x = 1
for i in range(100):
    if (x/5).is_integer() and (x/3).is_integer():
        print(" FizzBuzz")
    elif (x/3).is_integer():
        print (" Fizz")
    elif (x/5).is_integer():
        print(" Buzz")
    else:
        print (x)
    x = x+1
