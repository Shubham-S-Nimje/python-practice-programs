# Multiplication Table: Ask the user for a number and 
# print its multiplication table up to 10 using a for loop and range().

number = int(input("Enter any number :"))
for n in range(1,11,1):
    print(f'{n} X {number} = {n*number}')