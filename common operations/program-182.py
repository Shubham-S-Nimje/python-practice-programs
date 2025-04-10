# Count occurrences of an element in a list in Python
# input : a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# output: 1 --> 1
# 2 --> 2
# 3 --> 3
# 4 --> 4
# 1. Reading Unique elements (without duplicates)
# 2. Reading Unique elements from list and count in original list

a=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4,4,4,5,6,7,3,3,3]
b=[]
for value in a:
    if value not in b:
        b.append(value)
for value in b:
    c=a.count(value)
    print(f'{value}-->{c}')