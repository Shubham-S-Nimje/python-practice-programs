# >>> b1=b'ABC'
# >>> print(b1,type(b1))
# b'ABC' <class 'bytes'>
# >>> b1[0]
# 65
# >>> b1[1]
# 66
# >>> b1[2]
# 67
# >>> b2=B"ABC"
# >>> print(b2,type(b2))
# b'ABC' <class 'bytes'>
# >>> b2[0],b2[1],b2[2]
# (65, 66, 67)
# >>> b3=b'''ABC
# ... DEF'''
# >>> print(b3,type(b3))
# b'ABC\nDEF' <class 'bytes'>
# >>> for b in b3:
# ...     print(b)

# ... 
# ...     
# 65
# 66
# 67
# 10
# 68
# 69
# 70


# >>> b4=bytes(range(65,69))
# >>> print(b4,type(b4))
# b'ABCD' <class 'bytes'>
# >>> b5=bytes([65,66,67,68,69])
# >>> print(b5,type(b5))
# b'ABCDE' <class 'bytes'>
# >>> b6=bytes(10)
# >>> print(b6,type(b6))
# b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' <class 'bytes'>
# >>> print(b6[0])
# 0
# >>> print(b6[1])
# 0
# >>> print(b6[2])
# 0
# >>> del b6[0]
# Traceback (most recent call last):
#   File "<pyshell#24>", line 1, in <module>
#     del b6[0]
# TypeError: 'bytes' object doesn't support item deletion
# >>> b6[0]=65
# Traceback (most recent call last):
#   File "<pyshell#25>", line 1, in <module>
#     b6[0]=65
# TypeError: 'bytes' object does not support item assignment
