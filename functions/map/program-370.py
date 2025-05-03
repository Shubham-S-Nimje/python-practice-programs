A=[1,2,3,4,5,6,7,8,9,10]
B=list(map(lambda n:n**2,A))
C=list(map(lambda n:str(n),A))
print(A,B,C,sep="\n")
X=["naresh","ramesh","suresh","kishore","rajesh"]
Y=list(map(lambda s:s.upper(),X))
print(X,Y,sep="\n")
list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
list3=list(map(lambda n1,n2:n1*n2,list1,list2))
print(list1,list2,list3,sep="\n")
str1="10 20 30 40 50"
list4=list(map(int,str1.split()))
print(list4)
n1,n2,n3,n4,n5=list4
print(n1,n2,n3,n4,n5)
n1,n2,n3,n4,n5=map(int,input().split())
print(n1,n2,n3,n4,n5)
