# Write a program to find input string is
# alphanumeric string without using isalnum method

str1=input("Enter any string")
ac=0
dc=0

for ch in str1:
    if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
        ac+=1
    elif ch>='0' and ch<='9':
        dc+=1


if ac+dc==len(str1):
    print("alphanumeric string")
else:
    print("not alphanumeric string")
