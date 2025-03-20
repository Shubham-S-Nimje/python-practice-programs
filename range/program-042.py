# Write a program to generate table for input number
# number : 5
# 5x1=5
# 5x2=10
# 5x3=15
# ...
# 5x10=50

sum = 0
number = int(input('Enter any number :'))
for n in range(1,11,1):
    print(f'{number} x {n} = {number * n}')
