# >>> s1="   nit   "
# >>> s2=s1.strip()
# >>> print(len(s1),len(s2))
# 9 3
# >>> print(s1)
#    nit   
# >>> print(s2)
# nit
# >>> s3="**$$##nit**$$$^"
# >>> s4=s3.strip("*$#^")
# >>> print(s3)
# **$$##nit**$$$^
# >>> print(s4)
# nit
# >>> s1="www.nareshit.com"
# >>> s2=s1.strip("w.com")
# >>> print(len(s1))
# 16
# >>> print(len(s2))
# 8
# >>> print(s1)
# www.nareshit.com
# >>> print(s2)
# nareshit
