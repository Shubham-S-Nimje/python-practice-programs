# Create ASCII dictionary
# {'A':65,'B':66,'C':67,....'Z':90}
# {97:'a',98:'b',99:'c',.....,'z':122}

dict1={chr(n):n for n in range(65,91)}
print(dict1)
dict2={n:chr(n) for n in range(97,123)}
print(dict2)
