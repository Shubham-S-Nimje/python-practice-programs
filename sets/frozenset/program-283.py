# Nested set

A={frozenset(range(1,6)),frozenset(range(10,60,10))}
print(A)
for s in A:
    print(s)
    for value in s:
        print(value,end=' ')
    print()

