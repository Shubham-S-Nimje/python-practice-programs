# Write a program to read details n students
# each student is having name, 2 subject marks

n=int(input("How Student Details ?"))
marks={input('Name:'):
       [int(input('Sub1Marks:')),int(input('Sub2Marks:'))]
       for i in range(n)}

for name,m in marks.items():
    print(f'{name}-->{m}')
