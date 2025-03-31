# Write a program to generate prime numbers from 3 to 50
# using nested while loop

num=3
while num<=50:
    i=1
    c=0
    while i<=num:
        if num%i==0:
           c=c+1
        i=i+1
    if c==2:
        print(num)
    num=num+1