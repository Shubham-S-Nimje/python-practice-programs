# >>> b1=bytearray()
# >>> print(b1,type(b1))
# bytearray(b'') <class 'bytearray'>
# >>> b1.append(65)
# >>> b1.append(66)
# >>> b1.append(67)
# >>> print(b1,type(b1))
# bytearray(b'ABC') <class 'bytearray'>
# >>> del b1[0]
# >>> print(b1,type(b1))
# bytearray(b'BC') <class 'bytearray'>
# >>> b1[0]=65
# >>> print(b1,type(b1))
# bytearray(b'AC') <class 'bytearray'>
# >>> b2=bytearray(range(65,69))
# >>> print(b2,type(b2))
# bytearray(b'ABCD') <class 'bytearray'>
# >>> b3=bytearray([65,66,67,68,69])
# >>> print(b3,type(b3))
# bytearray(b'ABCDE') <class 'bytearray'>
# >>> b4=bytearray(5)
# >>> print(b4,type(b4))
# bytearray(b'\x00\x00\x00\x00\x00') <class 'bytearray'>
# >>> for b in b4:
# ...     print(b)
# ... 
# ...     
# 0
# 0
# 0
# 0
# 0
