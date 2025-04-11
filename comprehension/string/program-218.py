# >>> s1="PYTHON"
# >>> s1[0]
# 'P'
# >>> s1[1]='J'
# Traceback (most recent call last):
#   File "<pyshell#38>", line 1, in <module>
#     s1[1]='J'
# TypeError: 'str' object does not support item assignment
# >>> del s1[0]
# Traceback (most recent call last):
#   File "<pyshell#39>", line 1, in <module>
#     del s1[0]
# TypeError: 'str' object doesn't support item deletion
# >>> s1.append("K")
# Traceback (most recent call last):
#   File "<pyshell#40>", line 1, in <module>
#     s1.append("K")
# AttributeError: 'str' object has no attribute 'append'
