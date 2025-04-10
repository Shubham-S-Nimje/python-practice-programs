# Write a program to add two matices
# read 2x2 matrix

A=[]
B=[]
C=[]
print('Enter values of first matrix')

for i in range(2):
    row=[]
    for j in range(2):
        value=int(input('Enter value :'))
        row.append(value)
    A.append(row)

print('Enter values of second matrix')
for i in range(2):
    row=[]
    for j in range(2):
        value=int(input('Enter value :'))
        row.append(value)
    B.append(row)

for i in range(2):
    row=[]
    for j in range(2):
        row.append(A[i][j]+B[i][j])
    C.append(row)

print(f'A matrix {A}')
print(f'B matrix {B}')
print(f'C matrix {C}')