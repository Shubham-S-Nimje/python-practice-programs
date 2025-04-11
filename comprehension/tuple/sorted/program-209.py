# Python | Multiply Adjacent elements

'''
The original tuple : (1, 5, 7, 8, 10)
Resultant tuple after multiplication : (5, 35, 56, 80)
'''

A=(1, 5, 7, 8, 10)
B=tuple([A[i]*A[i+1] for i in range(len(A)-1)])
print(A)
print(B)
