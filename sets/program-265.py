# Task
# Now, let's use our knowledge of sets and help Mickey.
# Ms. Gabriel Williams is a botany professor at District College. 
# One day, she asked he student Mickey to compute the average of all 
# the plants with distinct heights in her greenhouse.

# Formula used:
# Average = Total Number of Distinct Heights / Sum of Distinct Heights


# Input Format
# The first line contains the integer, N, the size of arr.
# The second line contains the N space-separated integers, arr[i].

n=int(input("How many plants?"))
plants_height=set(map(int,input().split()))
print(plants_height)
avg=sum(plants_height)/len(plants_height)
print(f'{avg:.3f}')
