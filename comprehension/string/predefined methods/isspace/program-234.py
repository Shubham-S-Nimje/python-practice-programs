# >>> s1="     "
# >>> s1.isspace()
# True
# >>> s2="ab cd"
# >>> s2.isspace()
# False
# Write a program to find input string
# is alpbetic string or not without
# using isalpha method

str1=input("Enter any string ")
c=0

for ch in str1:
    if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
        c=c+1


if len(str1)==c:
    print("Alpahbetic String")
else:
    print("Not Alphabetic String")


