# write a program to print math table of input number
# using while loop

number = int(input("Enter any number :"))
i = 1
while(i <= 10):
    print(f'{number} x {i} = {number * i}')
    i = i + 1