A=[10,20,30,40,50]
# Write for loop read values from right to left using index
for i in range(-1,-(len(A)+1),-1):
  print(A[i],end=' ')
# Write for loop read values from left to right using -ve index
print()
for i in range(-len(A),0,1):
  print(A[i],end=' ')
# Write a for loop read values from right to left using +ve index
print()
for i in range(len(A)-1,-1,-1):

  print(A[i],end=' ')