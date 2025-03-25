# Write a program to print sum of digits of
# input number

number = int(input("Enter any number :"))

sum = 0
while(number > 0):
    d = number % 10
    sum = sum + d
    number = number // 10
print(f'sum is : {sum}')