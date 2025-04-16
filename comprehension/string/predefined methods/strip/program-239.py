# >>> str1="   nit"
# >>> len(str1)
# 6
# >>> str2=str1.lstrip()
# >>> print(str1)
#    nit
# >>> print(str2)
# nit
# >>> print(len(str2))
# 3
# >>> str3="****nit"
# >>> print(len(str3))
# 7
# >>> str4=str3.lstrip("*")
# >>> print(str4)
# nit
# >>> str5="**$$^^nit"
# >>> str6=str5.lstrip("*$^")
# >>> print(str5)
# **$$^^nit
# >>> print(str6)
# nit
# >>> str7="**n*i*t*"
# >>> str8=str7.lstrip("*")
# >>> print(str7)
# **n*i*t*
# >>> print(str8)
# n*i*t*
