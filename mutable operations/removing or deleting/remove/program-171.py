# Write a program to remove all occurences of given value
# from list using remove method
A=[10,20,30,20,20,20,30,40,50,20,20]
value=20
print(f'Before Deleting {A}')
while True:
    if value in A:
       A.remove(value)
    else:
      break
print(f'After Deleting {A}')

# Before Deleting [10, 20, 30, 20, 20, 20, 30, 40, 50, 20, 20]
# After Deleting [10, 30, 30, 40, 50]