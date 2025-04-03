# Write a program to count prime numbers in given list

A=[7,12,9,13,15,21,24,46]
prime_count=0
for i in range(len(A)):
  num=A[i]
  k=0
  for j in range(1,num+1):
   if num%j==0:
    k=k+1
  if k==2:
    print(num)
    prime_count=prime_count+1
print(f'List {A}')
print(f'Prime Number Count {prime_count}')