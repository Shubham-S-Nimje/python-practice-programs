# Factorial Calculation: Write a program that calculates 
# the factorial of a number using a for loop and range().

number = int(input("Enter any number :"))
factorial = 1
for n in range(1,number + 1,1):
    factorial = factorial * n
print(f'Factorial is {factorial}')