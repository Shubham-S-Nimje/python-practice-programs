# Python program to capitalize the first and last
# character of each word in a string

# input : python programming language
# output :PythoN ProgramminG LanguagE

str1="python programming language"

words = str1.split()

result = []

for w in words:
    w = w.lower()
    list2 = list(w)
    list2[0] = list2[0].upper()
    list2[-1] = list2[-1].upper()
    w = ''.join(list2)
    result.append(w)

print(' '.join(result))
