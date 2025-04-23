# Python – Avoid Spaces in string length

str1="abc xyz pqr"

count = 0

for i in str1:
    if i != ' ':
        count = count + 1
print(count)