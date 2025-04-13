# Remove All Duplicates from a Given String in Python

str1=input("Enter any string ")
str2=""

for ch in str1:
    if ch not in str2:
        str2=str2+ch


print(str1)
print(str2)
