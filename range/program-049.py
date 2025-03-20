#Python Program to Print the
# Natural Numbers Summation Pattern
#Given a natural number n, the task is to
# write a Python program to first find the sum of
# first n natural numbers and then print each step
# as a pattern
#Input: 5

#1 = 1
#1 + 2 = 3
#1 + 2 + 3 = 6
#1 + 2 + 3 + 4 = 10
#1 + 2 + 3 + 4 + 5 = 15

number = int(input('Enter any number :'))

for n in range(1, number + 1, 1):
    sum = 0
    for m in range(1, n + 1, 1):
        sum = sum + m
        if m != n:
            print(m, end = " + ")
        else:
            print(m, end = " = ")
    print(sum)