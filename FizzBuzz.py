#Project        FizzBuzz
#programmer     Justice Gutierrez
#Date           10/11/2022
#Description    Program should print numbers from 1-100
#               for each multiple of 3 it should write Fizz
#               for multiples of 5 it should write Buzz
#               and for multiples of both it should write FizzBuzz

#Variables
x = 1
#Counts from 1 to 100 and Writes each number or one of the following Fizz, Buzz, FizzBuzz
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
