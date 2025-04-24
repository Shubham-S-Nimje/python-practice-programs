# Write a program to read the marks details of n students
# each student having name,2 subject marks

# name --> key string
# 2 subject marks --> values []

student_marks={}
n=int(input("How Many Students?"))
for i in range(n):
    name=input("Enter Name ")
    if name not in student_marks:
        marks=[int(input("Enter Marks ")) for j in range(2)]
        student_marks[name]=marks
        print("Student Marks Added...")
    else:
        print(f'{name} exists')

print(student_marks)
for name,marks in student_marks.items():
    total=sum(marks)
    avg=total/2
    result="pass" if marks[0]>=40 and marks[1]>=40 else "fail"
    print(f'{name}\t{marks}\t{total}\t{avg:.2f}\t{result}')
