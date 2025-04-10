# Write a program to create list with sqr's all
# integer values which range from 1 to 10

# without comprehension
A=[]
for num in range(1,11):
    A.append(num**2)
print(A)

# with comprehension
B=[num**2 for num in range(1,11)]
print(B)
