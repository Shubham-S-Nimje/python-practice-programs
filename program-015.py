# Write a program to find a person elg for loan or not
# input credit score
# credit score&gt;=700 ==&gt; elg to apply loan
# credit score&lt;700 ==&gt; not elg to apply loan

cs = int(input("Enter credit score :"))

if cs >= 700:
    print("elg to apply loan")
else:
    print("not elg to apply loan")