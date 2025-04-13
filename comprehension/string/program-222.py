# Write a program to find maximum frequence
# character and minimum frequence character

str1=input("Enter any string ")
str2=""

for ch in str1:
    if ch not in str2:
        str2=str2+ch

print(str1)
print(str2)
A=[]
for ch in str2:
    c=str1.count(ch)
    A.append([c,ch])

print(A)
m1=max(A)
m2=min(A)
print(f'Maximum frequence character {m1[0]},{m1[1]}')
print(f'Minimum frequence character {m2[0]},{m2[1]}')
