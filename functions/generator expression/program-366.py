even_gen=(value for value in range(1,11) if value%2==0)
odd_gen=(value for value in range(1,11) if value%2!=0)
for value in even_gen:
    print(value,end=' ')
print()
for value in odd_gen:
    print(value,end=' ')
print()
