def power(num,p): # Required Parameters
    res=num**p
    return res



a=power(5,2) # Positional Arguments
print(a)
b=power(num=6,p=3) # Keyword Arguments
print(b)
c=power(p=2,num=10) # Keyword Arguments
print(c)
