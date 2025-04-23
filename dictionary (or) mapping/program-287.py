# zip(*iterables)
# Iterate over several iterables in parallel, producing tuples with 
# an item from each one.

# >>> d4=dict(zip("ABCDE",range(10,60,10)))
# >>> print(d4)
# {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}
# >>> d5=dict(zip([1,2,3],[10,20,30]))
# >>> print(d5)
# {1: 10, 2: 20, 3: 30}
# >>> d6=dict(zip(range(1,6),range(10,60,10)))
# >>> print(d6)
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# >>>
