# Using dict() function, dict() function is used to convert other iterables 
# or collections into dictionary type. Whenever we convert other 
# iterables/collections into dictionary type, that iterable must generate 
# two values.

# Syntax-1: dict()    : Create empty dictionary 
# Syntax-2: dict(iterable) : Create dictionary by converting other iteables

# >>> d1=dict()
# >>> print(d1)
# {}
# >>> print(type(d1))
# <class 'dict'>
# >>> A=[10,20,30]
# >>> d2=dict(A)
# Traceback (most recent call last):
#   File "<pyshell#57>", line 1, in <module>
#     d2=dict(A)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
# >>> A=[(1,10),(2,20),(3,30),(4,40),(5,50)]
# d2=dict(A)
# print(d2)
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# >>> X=[1,2,3]
# >>> Y=[10,20,30]
# >>> Z=[(X[i],Y[i]) for i in range(3)]
# >>> print(X,Y,Z,sep="\n")
# [1, 2, 3]
# [10, 20, 30]
# [(1, 10), (2, 20), (3, 30)]
# >>> d3=dict(Z)
# >>> print(d3)
# {1: 10, 2: 20, 3: 30}
