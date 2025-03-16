# You are building a program to check if a person is eligible to vote. 
# A person is eligible to vote if they are 18 years or older. 
# Write a Python function that takes the person's age as input and 
# prints "Eligible to vote" if the person is 18 or older, and 
# nothing otherwise.

age = int(input("Enter age :"))
if age >= 18:
    print(f'Eligible for vote')