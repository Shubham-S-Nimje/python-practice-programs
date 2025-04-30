def swap(x,index1,index2):
    x[index1],x[index2]=x[index2],x[index1]



A=[10,20,30,40,50]
print(f'Before swaping {A}')
swap(A,0,-1)
print(f'After swaping {A}')
