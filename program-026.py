# A program needs to check whether a person is an adult or a minor. 
# An adult is defined as anyone aged 18 or older. Write a Python 
# program that takes the person's age as input and prints "Adult" 
# if the person is 18 or older, and "Minor" otherwise.

age = int(input("Enter age :"))
if age >= 18:
    print(f'Adult')
else: print(f'Minor')