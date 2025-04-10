# Write a program to read 3x3 matrix and display
# upper triangle and lower triangle

A=[]
print("Input Values of matrix")
for i in range(3):
    row=[]
    for j in range(3):
        value=int(input("Enter value "))
        row.append(value)
    A.append(row)

print("Matrix")
for i in range(3):
    for j in range(3):
        print(A[i][j],end=' ')
    print()

print("Upper Triangle")
for i in range(3):
    for j in range(3):
        if j>=i:
            print(A[i][j],end=' ')
        else:
            print(' ',end=' ')
    print()
        
print("Lower Triangle")
for i in range(3):
    for j in range(3):
        if j<=i:
            print(A[i][j],end=' ')
    print()
