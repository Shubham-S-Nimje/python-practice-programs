# Write a program to count vowels in a given string

str1 = input('Enter any string :')
count = 0
vowels = 'aeiouAEIOU'

# for ch in str1:
#     for vo in vowels:
#         if vo == ch:
#             count = count + 1
# print(count)

for ch in str1:
    if ch in 'AEIOUaeiou':
        count=count+1
print(f'Vowel count {count}')