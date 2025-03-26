# Write a program to reverse number
# 123 ==> 321

number = int(input("Enter any number :"))

rev = 0
while(number > 0):
    d = number % 10
    rev = rev * 10 + d
    number = number // 10
print(f'Reverse is: {rev}')