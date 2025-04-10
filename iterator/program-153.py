A=[10,20,30,40,50]
x=iter(A)
n1=next(x)
n2=next(x)
n3=next(x)
n4=next(x)
n5=next(x)
print(n1,n2,n3,n4,n5)
B=list(range(10,110,10))
y=iter(B)
for n in y:
    print(n) 