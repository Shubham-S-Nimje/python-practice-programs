# >>> s1="aBCd"
# >>> s2=s1.swapcase()
# >>> print(s1)
# aBCd
# >>> print(s2)
# AbcD

# Write a program to convert string to
# uppercase without using upper() method

str1=input("Enter any string ")
str2=""

for ch in str1:
   if ch>='a' and ch<='z':
       str2=str2+chr(ord(ch)-32)
   else:
       str2=str2+ch

print(str1)
print(str2)
