A=[10,20,30,40,50]
x=iter(A) # Predefined iterator object
n1=next(x)
n2=next(x)
n3=next(x)
print(n1,n2,n3)

# developing generator
def riter(iterable): 
    for value in iterable[::-1]:
        yield value

# create iterator object
y=riter(A)
# read values by calling next function
n1=next(y)
n2=next(y)
n3=next(y)
print(n1,n2,n3)