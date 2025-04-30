def fun1(*a,**b):
    print(a,b,type(a),type(b))



fun1()
fun1(10)
fun1(x=10)
fun1(10,x=100)
fun1(10,20,30,x=100,y=200,z=300)
