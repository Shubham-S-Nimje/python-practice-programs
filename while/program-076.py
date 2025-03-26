# Write a program to count even and odd number digits in
# input number
# 1587

number = int(input("Enter any number :"))

sum = 0
evenc = 0
oddc = 0
while(number > 0):
    d = number % 10
    if d % 2 == 0:
        evenc = evenc + 1
    else:
        oddc = oddc + 1
    number = number // 10
print(f'Event Count: {evenc}, Odd Count: {oddc}')