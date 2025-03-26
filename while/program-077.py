# Write a program to print sum of even and odd digits
# in a given number

number = int(input("Enter any number :"))

sum = 0
evenc = 0
oddc = 0
while(number > 0):
    d = number % 10
    if d % 2 == 0:
        evenc = evenc + d
    else:
        oddc = oddc + d
    number = number // 10
print(f'Event Count: {evenc}, Odd Count: {oddc}')