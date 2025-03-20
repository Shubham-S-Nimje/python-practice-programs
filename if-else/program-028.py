# You are creating a login system. If the entered username 
# and password are correct, print "Login successful." Otherwise, 
# print "Login failed." Write a Python program that checks if both 
# the username and password are correct using if..else.

username = input("Enter username :")
password = float(input("Enter password :"))

if ((username == "shubham") & (password == 1234)):
    print(f"Login successful.")
else:
    print(f"Login failed.")