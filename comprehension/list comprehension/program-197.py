A=[1,2,5,7,8,9,3,11,13,6,24,15,18]

# create a list by adding even numbers
B=[value for value in A if value%2==0]
# create a list by adding odd numbers
C=[value for value in A if value%2!=0]

print(f'A list {A}')
print(f'B list {B}')
print(f'C list {C}')
