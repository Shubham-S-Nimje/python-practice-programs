# intersection_update(*others)
# set &= other & ...
# Update the set, keeping only elements found in it and all others.

# >>> A={1,2,3,4,5}
# >>> B={1,2,3,6,7}
# >>> A.intersection_update(B)
# >>> print(A)
# {1, 2, 3}
