# Python – Adding Tuple to List and Vice – Versa
# Note: concatenation is done with similar types
# but not different types of sequences

A=[10,20,30]
B=(40,50,60)

C=A+list(B)
print(A,B,C,sep="\n")
D=B+tuple(A)
print(A,B,D,sep="\n")

# [10, 20, 30]
# (40, 50, 60)
# [10, 20, 30, 40, 50, 60]
# [10, 20, 30]
# (40, 50, 60)
# (40, 50, 60, 10, 20, 30)