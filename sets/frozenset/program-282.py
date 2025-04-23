# >>> A=frozenset()
# >>> print(A,type(A))
# frozenset() <class 'frozenset'>
# >>> A.add(10)
# Traceback (most recent call last):
#   File "<pyshell#8>", line 1, in <module>
#     A.add(10)
# AttributeError: 'frozenset' object has no attribute 'add'
# >>>
# >>> B=frozenset(range(10,110,10))
# >>> print(B)
# frozenset({100, 70, 40, 10, 80, 50, 20, 90, 60, 30})
# >>> C=frozenset("PYTHON")
# >>> print(C)
# frozenset({'Y', 'P', 'N', 'H', 'O', 'T'})
# >>> D=frozenset([10,20,30,40,50])
# >>> print(D)
# frozenset({40, 10, 50, 20, 30})
# >>> E=frozenset({10,20,30,40,50})
# >>> print(E)
# frozenset({50, 20, 40, 10, 30})
# >>> F=frozenset((10,20,30,40,50))
# >>> print(F)
# frozenset({40, 10, 50, 20, 30})
