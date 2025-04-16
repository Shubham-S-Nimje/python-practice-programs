# >>> s1="nit****"
# >>> s2="nit    "
# >>> s3=s1.rstrip("*")
# >>> s4=s2.rstrip()
# >>> print(s1,s2,s3,s4,sep="\n")
# nit****
# nit    
# nit
# nit
# >>> s5="nit**$$@@"
# >>> s6=s5.rstrip("*$@")
# >>> print(s5)
# nit**$$@@
# >>> print(s6)
# Nit
