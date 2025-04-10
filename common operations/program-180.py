# index i and before index j)

# >>> A=[10,20,30,40,50]
# >>> A.index(30)
# 2
# >>> A.index(50)
# 4
# >>> A.index(80)
# Traceback (most recent call last):
# File '<pyshell#3>', line 1, in <module>
# A.index(80)
# ValueError: 80 is not in list
# >>> B=[10,20,30,40,10,10,10,20,20,40,50]
# >>> B.index(40)
# 3
# >>> B.index(40,5)
# 9
# >>> B.index(40,5,8)
# Traceback (most recent call last):
# File '<pyshell#7>', line 1, in <module>
# B.index(40,5,8)
# ValueError: 40 is not in list