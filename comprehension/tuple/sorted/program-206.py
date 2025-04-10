# Python – Maximum and Minimum K elements in Tuple
'''
Sometimes, while dealing with tuples,
we can have problem in which we need to
extract only extreme K elements,
i.e maximum and minimum K elements in Tuple.
This problem can have applications across domains
such as web development and Data Science

Input : test_tup = (3, 7, 1, 18, 9), k = 2 
Output : (3, 1, 9, 18)
'''

test_tup=(3, 7, 1, 18, 9)
k=2 

tup1=tuple(sorted(test_tup))
print(test_tup)
print(tup1)
tup2=tup1[:k]
tup3=tup1[-k:]

print(tup2)
print(tup3)
