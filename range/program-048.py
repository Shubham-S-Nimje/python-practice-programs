# Write a program to find input number is prime no or not

number = int(input('Enter any number :'))

check = 0
for n in range(1, number + 1, 1):
    if number % n == 0:
        check = check + 1

if check == 2:
    print(f'{number} is prime')
else:
    print(f'{number} is not prime')

