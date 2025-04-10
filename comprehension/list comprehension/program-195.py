# Write a program to create 2x2 matrix and display

# without comprehension
A=[]
for i in range(2):
    row=[]
    for j in range(2):
        value=int(input("Input Value "))
        row.append(value)
    A.append(row)

print(A)

# with comprehension
B=[[int(input("Input value")) for j in range(2)] for i in range(2)]
print(B)
