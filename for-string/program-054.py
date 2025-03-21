# Write a program to input string and count
# uppercase letters and lowercase letters

str1 = input('Enter any string :')
countUpper = 0
countLower = 0

for ch in str1:
    if ch>="A" and ch<="Z":
        countUpper = countUpper + 1
    if ch>="a" and ch<="z":
        countLower = countLower + 1
print(countUpper, countLower)