def maximum(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2

def is_prime(num):
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c+=1
    return c==2

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

def vowel_count(s):
    c=0
    for ch in s:
        if ch in "aeiouAEIOU":
            c+=1
    return c


res1=maximum(10,20)
res2=is_prime(5)
res3=factorial(4)
res4=vowel_count("java")
print(res1,res2,res3,res4,sep="\n")
