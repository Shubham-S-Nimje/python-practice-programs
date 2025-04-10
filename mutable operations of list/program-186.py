# Reading elements from matrix (nested list)

A=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# using index
for i in range(4):
    for j in range(3):
        print(A[i][j],end=" ")
    print()

# using for loop
for row in A:
    for value in row:
        print(value,end=" ")
print()