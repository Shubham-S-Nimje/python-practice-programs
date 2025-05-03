r1=range(1,11)
for value in r1:
    print(value,end=' ')

def float_range(start,stop,step=1.0):
    if start<stop:
        while start<stop:
            yield start
            start=start+step
    elif start>stop:
        while start>stop:
            yield start
            start=start+step

print()
r2=float_range(1.0,11.0)
for value in r2:
    print(value,end=' ')
print()
r3=float_range(10.0,0.0,-1.0)
for value in r3:
    print(value,end=' ')
print()
r4=float_range(1,10,1)
for value in r4:
    print(value,end=' ')
