# Write a program to input 5 values within list

# without comprehension

A=[]
for i in range(5):
    value=int(input("Enter value "))
    A.append(value)

print(A)

# with comprehension
B=[int(input("Enter Value")) for i in range(5)]
print(B)
