# Python program to check if a string has at least one letter
# and one number

str1=input("Enter any string ")
ac=0
dc=0

for ch in str1:
    if ch.isalpha():
        ac=ac+1
    elif ch.isdigit():
        dc=dc+1

if ac>0 and dc>0:
    print("string contains one letter and digit")
else:
    print("string does not contains one letter or digit")
