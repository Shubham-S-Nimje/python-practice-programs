# Write a program to print sum of numbers
# input numbers until user input number is equal to -1

s=0
while True:
  num=int(input('Enter any number:'))
  if num==-1:
    break
s=s+num
print(f'Sum is {s}')