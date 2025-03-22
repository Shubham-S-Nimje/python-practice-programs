# Finding Prime Numbers: Use a for loop and range() to check 
# if a given number is prime.

number = int(input("Enter any number :"))
count = 0
for n in range(1,number + 1,1):
    if number % n == 0:
        count = count + 1

if count == 2:
    print(f'{number} is prime number')
else:
    print(f'{number} is not prime number')