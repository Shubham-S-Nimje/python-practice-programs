# Write a program to generate input number is prime
# or not using while loop

number = int(input("Enter any number :"))
i = 1
count = 0
while(i <= number):
    if number % i == 0:
        count = count + 1
    i = i + 1
if count == 2:
    print(f'{number} is prime')
else:
    print(f'{number} is not prime')