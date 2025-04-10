# >>> names=['naresh','ramesh','kishore','rajesh','kiran']
# >>> names.remove('kishore')
# >>> print(names)
# ["naresh", "ramesh", "rajesh", "kiran"]
# >>> names.remove('naresh')
# >>> print(names)
# ["ramesh", "rajesh", "kiran"]
# >>> names.remove('naresh')
# Traceback (most recent call last):
# File '<pyshell#22>', line 1, in &lt;module>
# names.remove('naresh')

# ValueError: list.remove(x): x not in list
# >>> A=[10,20,30,20,20,30,40]
# >>> print(A)
# [10, 20, 30, 20, 20, 30, 40]
# >>> A.remove(20)
# >>> print(A)
# [10, 30, 20, 20, 30, 40]