# Create a dictionary with n items
# each item consist of two values
# key --> number
# value --> sqr of number


# without comprehension
n=int(input("How many integers ?"))
dict1={}
for num in range(1,n+1): # 1 2 3 4 ... n
    dict1[num]=num**2

print(dict1)

# with comprehension
dict2={num:num**2 for num in range(1,n+1)}
print(dict2)
