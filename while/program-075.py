# Write a program to find input number is
# armstrong number or not (3 digit number)
# An Armstrong number is a number where the sum of its digits,
# each raised to the power of the number of digits,
# equals the number itself

number = int(input("Enter any number :"))

sum = 0
num = number
while(number > 0):
    d = number % 10
    sum = sum + d**3
    number = number // 10
if sum == num:
    print(f'{num} is Armstrong')
else:
    print(f'{num} is not Armstrong')