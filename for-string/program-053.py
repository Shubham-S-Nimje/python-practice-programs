# Write a program to input string and count

# str1 = input('Enter any string :')
# count = 0

# for ch in str1:
#     count = count + 1
# print(count)


# uppercase letters

str1 = input('Enter any string :')
count = 0

for ch in str1:
    if ch>="A" and ch<="Z":
        count = count + 1
print(count)