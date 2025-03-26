# A
# A B
# A B C
# A B C D
# A B C D E

for m in range(65, 70):
    for n in range(65, m + 1):
        print(chr(n), end=" ")
    print()