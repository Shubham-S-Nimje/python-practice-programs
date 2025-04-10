# Write a program to add two matrices

print("Enter values of first matrix")
A=[[int(input("Input value")) for j in range(2)] for i in range(2)]
print("Enter values of second matrix")
B=[[int(input("Input Value")) for j in range(2)] for i in range(2)]

C=[[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]
print(A)
print(B)
print(C)
