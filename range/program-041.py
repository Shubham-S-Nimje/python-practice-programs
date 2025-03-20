# Write a program to input 5
# numbers and print sum

sum = 0

for n in range(1,6,1):
    number = int(input(f'Enter {n} number :'))
    sum = sum + number
print(f'Sum is {sum}')


