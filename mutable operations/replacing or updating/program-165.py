# To swap two elements in a list
# Swap first two elements with last two elements and
# last two elements with first two elements
A=[10,20,30,40,50,60,70,80,90,100]
print(f'Before Swaping {A}')
A[0:2],A[-2:]=A[-2:],A[0:2]
print(f'After Swaping {A}')

# Before Swaping [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# After Swaping [90, 100, 30, 40, 50, 60, 70, 80, 10, 20]