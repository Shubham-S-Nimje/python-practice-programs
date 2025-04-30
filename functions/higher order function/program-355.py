def calculator(a,b,function):
    c=function(a,b)
    return c

def add(n1,n2):
    n3=n1+n2
    return n3
def sub(n1,n2):
    n3=n1-n2
    return n3

res1=calculator(5,2,add)
res2=calculator(5,2,sub)
print(res1,res2,sep="\n")
res3=calculator(2,3,pow)
print(res3)
