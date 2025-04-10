# >>> test_tup=(3, 7, 1, 18, 9)
# >>> test_tup.sort()
# Traceback (most recent call last):
#   File "<pyshell#31>", line 1, in <module>
#     test_tup.sort()
# AttributeError: 'tuple' object has no attribute 'sort'
# >>> a=sorted(test_tup)
# >>> print(a)
# [1, 3, 7, 9, 18]
# >>> b=sorted(test_tup,reverse=True)
# >>> print(b)
# [18, 9, 7, 3, 1]
# >>> print(test_tup)
# (3, 7, 1, 18, 9)
