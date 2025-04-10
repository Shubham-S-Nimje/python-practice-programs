# How to create tuple?
# Tuples may be constructed in a number of ways:
# Using a pair of parentheses to denote the empty tuple: ()
# Using a trailing comma for a singleton tuple: a, or (a,)
# Separating items with commas: a, b, c or (a, b, c)
# Using the tuple() built-in: tuple() or tuple(iterable)


# Creating empty tuple using ()

# >>> t1=()
# >>> print(t1,type(t1))
# () <class 'tuple'>
# >>> L1=[]
# >>> print(L1,type(L1))
# [] <class 'list'>
# L1.append(10)
# >>> print(L1)
# [10]
# >>> t1.append(10)
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     t1.append(10)
# AttributeError: 'tuple' object has no attribute 'append'
