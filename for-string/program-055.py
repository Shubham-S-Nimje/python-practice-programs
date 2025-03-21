# Write a program to count alphabets, digits and
# special characters in a given string

str1 = input('Enter any string :')
countUpper = 0
countLower = 0
countDigit = 0
countSpeChar = 0

for ch in str1:
    if ch>="A" and ch<="Z":
        countUpper = countUpper + 1
    elif ch>="a" and ch<="z":
        countLower = countLower + 1
    elif ch>='0' and ch<='9':
        countDigit = countDigit + 1
    elif ch>='0' and ch<='9':
        countDigit = countDigit + 1
    else:
        countSpeChar = countSpeChar + 1
print(countUpper, countLower, countDigit, countSpeChar)