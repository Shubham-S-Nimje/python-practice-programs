# Write a program to find max of 3 numbers
num1 = int(input('Enter first number :'))
num2 = int(input('Enter second number :'))
num3 = int(input('Enter third number :'))

result = num1 if num1 > num2 and num1 > num3 else num2 if num2 > num1 and num2 > num3 else num3
print(f'max of {num1} and {num2} and {num3} id {result}')