# Write a program to find input number is pal or not
# 121 ==> 121

number = int(input("Enter any number :"))

rev = 0
num = number
while(number > 0):
    d = number % 10
    rev = rev * 10 + d
    number = number // 10

if num == rev:
    print(f'Given number is pal')
else: 
    print(f'Given number is not pal')