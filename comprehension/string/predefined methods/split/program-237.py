# Write a program to find maximum length word
# within string
# str1 --> python programming language


str1="python programming language"
list1=str1.split()
print(list1)
s=max(list1,key=len)
print(s)
m=min(list1,key=len)
print(m)
