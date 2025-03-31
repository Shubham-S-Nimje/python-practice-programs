# Generate tables from 1 to 10 using nested while

num=1
while num<=10: # Outer loop (generating numbers)
    i=1
    while i<=10: # Inner loop (multiplying number 10 times)
        p=num*i
        print(f'{num}x{i}={p}')
        i=i+1
    num=num+1