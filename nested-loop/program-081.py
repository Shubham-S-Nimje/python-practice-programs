# Write a program to generate prime numbers from 3-50

for m in range(3,51):
    count = 0
    for n in range(1,m + 1):
        if m % n == 0:
            count = count + 1
    if count == 2:
        print(f'{m}')