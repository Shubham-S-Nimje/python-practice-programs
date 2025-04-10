#Create a List of Tuples with Numbers and Their Cubes – Python

'''
 For example, if the input is [1, 2, 3],
 the output should be [(1, 1), (2, 8), (3, 27)].'''

A=[1,2,3,4,5]
B=[(n,n**3) for n in A]

print(A)
print(B)
