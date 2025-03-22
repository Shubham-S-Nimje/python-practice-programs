# FizzBuzz Game: Print numbers from 1 to 50. If a number 
# is divisible by 3, print “Fizz”. If it is divisible by 5, 
# print “Buzz”. If it is divisible by both, print “FizzBuzz”.  

for number in range(1,51,1):
    if number % 3 == 0:
        print(f'{number} “Fizz”')
    if number % 5 == 0:
        print(f'{number} “Buzz”')
    if number % 3 == 0 and number % 5 == 0:
        print(f'{number} “FizzBuzz”')