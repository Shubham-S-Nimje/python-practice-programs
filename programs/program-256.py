# Python – Uppercase Half String
# input : python
# output : PYThon

str1="python"

half1 = str1[:len(str1)//2:]
half2 = str1[len(str1)//2::]

print(half1.upper() + half2)