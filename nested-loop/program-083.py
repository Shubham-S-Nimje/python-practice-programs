# Write a program to generate Armstrong numbers from 100 to 999

for num in range(100,1000):
    num1=num
    s=0
    for i in range(3):
        d=num%10
        s=s+(d**3)
        num=num//10
    if s==num1:
        print(num1)

# for m in range(100,1000):
#     num = m
#     count = 0
#     while m>0:
#         d=m%10
#         count=count+(d**3)
#         m=m//10
#     if num == count:
#         print(f'{num}')