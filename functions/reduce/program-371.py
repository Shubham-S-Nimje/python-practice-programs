import functools
A=[1,2,3,4,5,6,7,8,9,10]
res1=functools.reduce(lambda x,y:x+y,A)
res2=functools.reduce(lambda x,y:x*y,A)
res3=functools.reduce(lambda x,y:x if x>y else y,A)
res4=functools.reduce(lambda x,y:x if x<y else y,A)
print(res1,res2,res3,res4,sep="\n")
