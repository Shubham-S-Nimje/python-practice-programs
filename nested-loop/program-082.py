# Write a program to generate Armstrong numbers from 100 to 999

for m in range(100,1000):
    num = m
    count = 0
    while m>0:
        d=m%10
        count=count+(d**3)
        m=m//10
    if num == count:
        print(f'{num}')