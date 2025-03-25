# Write a program to generate factorial of
# input number

number = int(input("Enter any number :"))
i = 1
factorial = 1
while(i <= number):
    factorial = factorial * i
    i = i + 1
print(f'Factorial is : {factorial}')