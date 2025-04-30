def maximum(**k):
    if len(k)==0:
        return None
    else:
        max_value=0
        for x,y in k.items():
            if y>max_value:
                max_value=y
                t=(x,y)
        return t

res1=maximum(a=10,b=20,c=5)
print(res1)
res2=maximum(sub1=60,sub2=50,sub3=90)
print(res2)
