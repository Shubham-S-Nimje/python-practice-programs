# If value exists it remove value from set
# If value not exists it raises KeyError


# >>> A={10,20,30,40,50}
# >>> print(A)
# {50, 20, 40, 10, 30}
# >>> A.remove(20)
# >>> print(A)
# {50, 40, 10, 30}
# >>> A.remove(10)
# >>> print(A)
# {50, 40, 30}
# >>> A.remove(10)
# Traceback (most recent call last):
#   File "<pyshell#16>", line 1, in <module>
#     A.remove(10)
# KeyError: 10
