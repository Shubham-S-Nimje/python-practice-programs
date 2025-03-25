# Wrie a program to input a number and count digits or
# length number

number = int(input("Enter any number :"))

count = 0
while(number > 0):
    count = count + 1
    number = number // 10
print(f'count is : {count}')