# Least Frequent Character in String
# Maximum frequency character in String

str1="abaabcbaaadd"
str2=""

for ch in str1:
    if ch not in str2:
        str2=str2+ch

print(str2)
A=[]
for ch in str2:
    c=str1.count(ch)
    A.append((c,ch))

print(A)
t1=max(A)
t2=min(A)
print(t1)
print(t2)
