# Write a program to find factorial of input number

number = int(input('Enter any number :'))
fact = 1
for n in range(1,number+1,1):
    fact = fact * n
print(f'Factorial of {number} is {fact}')