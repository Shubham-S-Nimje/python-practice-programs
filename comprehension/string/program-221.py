# Write a program to find frequence of
# characters within string

# str1 --> abcaaabccd
# output -->4a2b3c1d

str1=input("Enter any string ")
str2=""

for ch in str1:
    if ch not in str2:
        str2=str2+ch

print(str1)
print(str2)
str3=""
for ch in str2:
    c=str1.count(ch)
    str3=str3+str(c)+ch

print(str3,end="")
