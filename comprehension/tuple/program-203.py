# Creating tuple using tuple() function
# Tuple() function is used to create tuple by converting other iterables into tuple type

# Syntax1: tuple()  : create empty tuple
# Syntax2: tuple(iterable) : This create tuple by converting other iterables into tuple

# >>> t1=tuple()
# >>> print(t1,type(t1))
# () <class 'tuple'>
# >>> t2=tuple(range(10,110,10))
# >>> print(t2)
# (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# >>>t3=tuple("PYTHON")
# print(t3)
# ('P', 'Y', 'T', 'H', 'O', 'N')
# >>> t4=tuple([10,20,30,40,50])
# >>> print(t4)
# (10, 20, 30, 40, 50)
# >>> t5=tuple((10,20,30,40,50))
# >>> print(t5)
# (10, 20, 30, 40, 50)
