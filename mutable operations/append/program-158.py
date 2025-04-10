# Write a program to remove duplicate values from list
A=[1,2,3,4,1,2,3,4,1,2,3,4]
B=[]
for value in A:
    if value not in B:
     B.append(value)
print(A)
print(B)