# >>> s1="ABC"
# >>> s1.isupper()
# True
# >>> s2="AbC"
# >>> s2.isupper()
# False
# >>> s3="ABC123"
# >>> s3.isupper()
# True
# name validation
# name must be given in capital letters

name=input("Enter Name ")
if name.isupper():
    print("valid")
else:
    print("invalid name must be uppercase")

