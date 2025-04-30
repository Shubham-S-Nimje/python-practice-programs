def sort(x,reverse=False):
    if reverse:
        for i in range(len(x)):
            for j in range(len(x)-1):
                if x[j]<x[j+1]:
                    x[j],x[j+1]=x[j+1],x[j]
    else:
        for i in range(len(x)):
            for j in range(len(x)-1):
                if x[j]>x[j+1]:
                    x[j],x[j+1]=x[j+1],x[j]

#main
A=[4,8,3,5,7,2,6,1]
print(f'Before Sorting {A}')
sort(A)
print(f'After Sorting {A}')
sort(A,reverse=True)
print(f'After Sorting {A}')
