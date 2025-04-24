# >>> d2={1:10,2:20,3:30,4:40,5:50}
# print(d2)
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# >>> a=d2.pop(1)
# >>> print(a)
# 10
# >>> print(d2)
# {2: 20, 3: 30, 4: 40, 5: 50}
# >>> b=d2.pop(5)
# >>> print(b)
# 50
# >>> print(d2)
# {2: 20, 3: 30, 4: 40}
# >>> c=d2.pop(6)
# Traceback (most recent call last):
#   File "<pyshell#49>", line 1, in <module>
#     c=d2.pop(6)
# KeyError: 6
# >>> c=d2.pop(6,None)
# >>> print(c)
# None
# >>> d=d2.pop(7,70)
# >>> print(d)
# 70
