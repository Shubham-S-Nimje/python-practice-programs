# How to Remove Letters From a String in Python

str1=input("Enter any string ")
list1=list(str1)
index=int(input("Index of character to remove"))

del list1[index]
str2=''.join(list1)

print(str1)
print(str2)
