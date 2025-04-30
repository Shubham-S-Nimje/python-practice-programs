def maximum(*a):
    if len(a)==0:
        return None
    else:
        max_value=a[0]
        for value in a:
            if value>max_value:
                max_value=value
        return max_value


res1=maximum()
print(res1)
res2=maximum(10)
print(res2)
res3=maximum(10,40,30,50,20)
print(res3)
