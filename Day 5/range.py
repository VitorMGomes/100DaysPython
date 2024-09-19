#for number in range(1, 10 + 1):
#    print(number)
    
#print()

#for number in range(1, 11, 3):
#    print(number)
    
for number in range(1, 101):
    if(number % 5 == 0 and number % 3 ==0):
        print("FizzBuzz")
    elif(number % 3 == 0):
        print("Fizz")
    elif(number % 5 == 0):
        print("Buzz")
    else:
        print(number)