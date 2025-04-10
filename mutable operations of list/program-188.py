# Write a program to read 3 students 2 subject marks and
# display

student=[]
for i in range(3):
    row=[]
    for j in range(2):
        s=int(input(f"Input Student{i+1} and Subject{j+1} "))
        row.append(s)
    student.append(row)
print(student)