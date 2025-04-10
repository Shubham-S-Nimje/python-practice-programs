# Write a program from given list separate even
# and odd numbers
A=[1,2,3,4,5,6,7,8,9,10,11,24,14,17,19,24]
even_list=[]
odd_list=[]
for value in A:
    if value%2==0:
      even_list.append(value)
    else:
      odd_list.append(value)
print(A)
print(even_list)
print(odd_list)