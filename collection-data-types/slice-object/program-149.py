even_slice=slice(0,10,2)

odd_slice=slice(1,10,2)
reverse_slice=slice(-1,-11,-1)
A=list(range(10,110,10))
print(A)
B=A[even_slice]
print(B)
C=A[odd_slice]
print(C)
D=A[reverse_slice]
print(D)