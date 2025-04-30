def sum_values(*vargs):
    s=0
    for value in vargs:
        s=s+value
    return s


res1=sum_values()
print(res1)
res2=sum_values(10)
res3=sum_values(10,20,30)
res4=sum_values(1,1.5,2.5,4)
print(res2,res3,res4,sep="\n")