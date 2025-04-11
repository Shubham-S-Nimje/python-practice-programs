# Write a program to count vowels within string

str1=input("Enter any string ")
c=0
for ch in str1:
    if ch in "aeiouAEIOU":
        c=c+1

print(f'String is {str1}')
print(f'Count of vowels {c}')


# Enter any string javascript
# String is javascript
# Count of vowels 3