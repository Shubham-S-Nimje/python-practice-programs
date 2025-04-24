# >>> dict1=dict(zip(range(1,11),range(10,110,10)))
# >>> print(dict1)
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90, 10: 100}
# >>> del dict1[1]
# >>> print(dict1)
# {2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90, 10: 100}
# >>> del dict1[8]
# >>> print(dict1)
# {2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 9: 90, 10: 100}
# >>> del dict1[1]
# Traceback (most recent call last):
#   File "<pyshell#36>", line 1, in <module>
#     del dict1[1]
# KeyError: 1
