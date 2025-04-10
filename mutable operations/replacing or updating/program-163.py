# To interchange first and last elements in a list
A=[10,20,30,40,50,60,70,80]
print(f'Before Swaping {A}')
A[0],A[-1]=A[-1],A[0]
print(f'After Swaping {A}')
x=A[0]
A[0]=A[-1]
A[-1]=x
print(f'After Swaping {A}')

# Before Swaping [10, 20, 30, 40, 50, 60, 70, 80]
# After Swaping [80, 20, 30, 40, 50, 60, 70, 10]
# After Swaping [10, 20, 30, 40, 50, 60, 70, 80]