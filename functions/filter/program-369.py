A=[1,2,3,4,5,6,7,8,9,10]
B=list(filter(lambda n:n%2==0,A))
C=list(filter(lambda n:n%2!=0,A))
print(A)
print(B)
print(C)
X=[1,2,3,-4,-5,6,-7,-8,9,-10,11,12]
Y=list(filter(lambda n:n>=0,X))
Z=list(filter(lambda n:n<0,X))
print(X,Y,Z,sep="\n")
list1=["naresh","RAMESH","kishore","RAJESH","KISHORE"]
list2=list(filter(lambda s:s.isupper(),list1))
list3=list(filter(lambda s:s.islower(),list1))
print(list1,list2,list3,sep="\n")
