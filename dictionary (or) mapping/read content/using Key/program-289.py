# Result Finding OR Result Processing

marks_dict={1:['naresh',60,70],
            2:['suresh',90,80],
            3:['kishore',50,40],
            4:['ramesh',70,30],
            5:['kiran',30,20]}

rollno=int(input("Rollno :"))

if rollno in marks_dict:
    student = marks_dict[rollno]
    name,sub1,sub2 = student

    if sub1 >= 40 and sub2 >= 40:
        print('Pass')
    else:
        print('Fail')
else:
    print("Invalid RollNo")