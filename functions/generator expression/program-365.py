cube_gen=(value**3 for value in range(1,11))
sqr_gen=(value**2 for value in range(1,11))
alpha_gen=(chr(value) for value in range(65,91))

for value in cube_gen:
    print(value,end=' ')
print()
for value in sqr_gen:
    print(value,end=' ')
print()
for value in alpha_gen:
    print(value,end=' ')
