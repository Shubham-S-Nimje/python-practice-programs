# Sort a List of Tuples by Second Item – Python

a=[(1, 3), (4, 1), (2, 2)]
print(f'List before sorting {a}')
a.sort()
print(f'List after sorting using first item of tuple {a}')

for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j][1]>a[j+1][1]:
            a[j],a[j+1]=a[j+1],a[j]


print(f'List after sorting using second item of tuple {a}')
