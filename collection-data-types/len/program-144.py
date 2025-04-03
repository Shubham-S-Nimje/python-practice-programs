# Write a program to find minimum and maximum from
# given list of values
A=[10,60,30,20,50,40]
for i in range(len(A)): # start=0,stop=6,step=1 0 1 2 3 4 5
  if i==0:
   max_value=A[i]
   min_value=A[i]
  elif A[i]>max_value:

    max_value=A[i]
  elif A[i]<min_value:
   min_value=A[i]
print(f'List is {A}')
print(f'Maximum Value {max_value}')
print(f'Minimum Value {min_value}')