# Write a program to read name, n subject marks
# calculate total marks, avg marks, min marks, max marks
name=input('Enter StudentName :')
marks=[]
n=int(input('How many subject marks?'))

for i in range(n):
    s=int(input(f'Enter Subject{i+1} Marks :'))
    marks.append(s)
total=sum(marks)
avg=total/n
min_marks=min(marks)
max_marks=max(marks)
print(f'''Name {name}
Marks {marks}
Total Marks {total}
Avg Marks {avg:.2f}
Minimum Marks {min_marks}
Maximum Marks {max_marks}''')