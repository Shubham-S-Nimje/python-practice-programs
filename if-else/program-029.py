# A car rental company has a policy where you can rent a car 
# if you are at least 21 years old. Write a Python program 
# that checks if the user is eligible to rent a car by using if..else. 
# If they are 21 or older, print "Eligible to rent a car," otherwise 
# print "Not eligible."


age = int(input("Enter age :"))
if age >= 21:
    print(f'Eligible to rent a car')
else: print(f'Not eligible.')