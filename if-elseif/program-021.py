# Given an integer,n , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of  2 to 5, print Not Weird
# If n is even and in the inclusive range of  6 to 20, print Weird
# If n  is even and greater than 20 , print Not Weird


n = int(input("Enter integer :"))

if n % 2 != 0:
    print(f"Weird")
elif n % 2 == 0 & 2 <= n <= 5:
    print(f"Not Weird")
elif n % 2 == 0 & 6 <= n <= 20:
    print(f"Weird")
else:
    print(f"Not Weird")