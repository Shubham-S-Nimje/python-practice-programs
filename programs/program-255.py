# Python program to print even length words in a string

str1="abc abcd xyz pq rstuv mn"
list1=str1.split()

for w in list1:
    if len(w)%2 == 0:
        print(w)