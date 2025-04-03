# Write a program to print sum of elements/items of list
A=[10,20,30,40,50,60,70,80,90,100]
s=0
for i in range(len(A)): # start=0,stop=10,step=1 0 1 2 3
    s=s+A[i]

print(f'List is {A}')
print(f'Sum of Elements {s}')