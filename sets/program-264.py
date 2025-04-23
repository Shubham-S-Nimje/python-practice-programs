# How to read content of set?
# Set is non index based collection; it does not support indexing 
# and slicing. We can read content of set of using “for” loop

# >>> A={10,20,30,40,50}
# >>> print(A)
# {50, 20, 40, 10, 30}
# >>> A[0]
# Traceback (most recent call last):
#   File "<pyshell#74>", line 1, in <module>
#     A[0]
# TypeError: 'set' object is not subscriptable
# >>> A[0:2]
# Traceback (most recent call last):
#   File "<pyshell#75>", line 1, in <module>
#     A[0:2]
# TypeError: 'set' object is not subscriptable
# >>> for num in A:
# ...     print(num)
# ... 
# ...     
# 50
# 20
# 40
# 10
# 30
