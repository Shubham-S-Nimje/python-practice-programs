# Python program to check whether the string is
# Symmetrical or Palindrome

str1=input("Enter any string ")
str2=str1[::-1] #str1[start:stop:step]

if str1 == str2:
    print('Palindrome')
else:
    print('Not Palindrome')

if len(str1)%2 == 0:
    half1 = str1[:len(str1)//2]
    half2 = str1[len(str1)//2::]
    
    if half1 == half2:
        print('Symmetrical')
    else:
        print('Not Symmetrical')
else:
    print('Not Symmetrical')
