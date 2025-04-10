# Write a program to read 2x2 matrix and display

matrix=[]
for i in range(2):
    row=[]
    for j in range(2):
        value=int(input("Enter value :"))
        row.append(value)
    matrix.append(row)
print(matrix)