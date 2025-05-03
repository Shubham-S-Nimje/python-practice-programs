# Generator Function
def fun1():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50
    
# Normal function
def fun2():
    return 10
    return 20
    return 30
    return 40
    return 50

x=fun1() # Create iterator object
y=fun2() # return value
print(x)
print(y)
n1=next(x)
print(n1)
n2=next(x)
print(n2)
n3=next(x)
print(n3)
