# Python program to find nth maximum in a list
a=[10,20,4,45,99,30,40,100,100,25]
b=[]

for value in a:
    if value not in b:
        b.append(value)

b.sort(reverse=True)
print(b)

n=int(input("enter value of n "))
if n>0 and n<len(b):
    print(f'{n}th maximum is {b[n-1]}')
else:
    print("invalid n value")