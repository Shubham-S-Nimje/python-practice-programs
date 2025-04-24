# Write a program to add n student details within
# dictionary
# each student is having name and course

students={}
n=int(input("How Many Students?"))

for i in range(n):
    name=input("Enter Name :")
    if name in students:
        print(f'{name} exists')
    else:
        course=input("Enter Course :")
        students[name]=course
        print("Student Added...")


print("Student Details")
for t in students.items():
    print(t)
