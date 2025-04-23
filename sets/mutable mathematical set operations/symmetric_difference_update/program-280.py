# symmetric_difference_update(other)
# set ^= other
# Update the set, keeping only elements found in either set, but not in both.

# >>> A={1,2,3,4,5}
# >>> B={1,2,3,6,7}
# >>> A.symmetric_difference_update(B)
# >>> print(A)
# {4, 5, 6, 7}