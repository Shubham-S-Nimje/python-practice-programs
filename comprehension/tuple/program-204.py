# tuple is immutable sequence and support indexing and slicing
t1=(10,20,30,40,50)
print(t1[0],t1[1],t1[2],t1[3],t1[4])
print(t1[-1],t1[-2],t1[-3],t1[-4],t1[-5])

x=t1[0:2]
y=t1[-1:-3:-1]
z=t1[::-1]

print(x,y,z,sep="\n")
