# Write a program to input name,age and find person
# is elg to vote or not


name = input("Enter Name :")
age = int(input("Enter age :"))
if age >= 18:
    print(f'{name} is eligible for voting')
else: print(f'{name} is not eligible for voting')