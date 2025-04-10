# Write a program to read 3x3 matrix and display transpose of
# matrix

A=[]
print('Input values of matrix')

for i in range(3):
    row=[]
    for j in range(3):
        value=input('Input values :')
        row.append(value)
    A.append(row)

print('Matrix is')

for i in range(3):
    for j in range(3):
        print(A[i][j],end=' ')
    print()
print('Matrix Transpose')

for i in range(3):
    for j in range(3):
        print(A[j][i],end=' ')
    print()