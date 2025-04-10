# Python program to find second largest number in a list
a=[10,20,4,45,99,30,40,100,100,25]
first_max=max(a)

print(f'First Maximum is {first_max}')
a.sort()
print(a)
print(f'First Maximum is {a[-1]}')
c=a.count(a[-1])
print(f'Second Maximum is {a[-(c+1)]}')

# First Maximum is 100
# [4, 10, 20, 25, 30, 40, 45, 99, 100, 100]
# First Maximum is 100
# Second Maximum is 99