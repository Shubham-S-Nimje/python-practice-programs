# Write a program in given count even and odd numbers
A=[4,9,2,3,6,1,11,13,15,18,21,24,54,7,9,3]
ec=0
oc=0
for i in range(len(A)):
    if A[i]%2==0:
      ec=ec+1
    else:
     oc=oc+1
print(f'List of values {A}')
print(f'Even Count {ec}')
print(f'Odd Count {oc}')