# Write a program to find max of three numbers

n1 = int(input("Enter first number :"))
n2 = int(input("Enter second number :"))
n3 = int(input("Enter third number :"))

if n1 >= n2:
    if n1 >= n3: 
        print(f'{n1} is max')
    else:
        print(f'{n3} is max')
elif n2 >= n1:
    if n2 >= n3:
        print(f'{n2} is max')
    else:
        print(f'{n3} is max')
elif n3 >= n1:
    if n3 >= n2:
        print(f'{n3} is max')
    else:
        print(f'{n2} is max')