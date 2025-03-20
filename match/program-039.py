# find area of different shapes
print('****MENU*****')
print('1.Area of Circle')
print('2.Area of Triangle')
print('3.Area of Rectangle')
print('4.Exit')

opt=int(input('Your Option :'))
match(opt):
    case 1:
        r=float(input('Enter radious of circle :'))
        a=3.147*r*r
        print(f'Area of circle is :{a:.2f}')
    case 2:
        base=float(input('Enter base of triangle :'))
        height=float(input('Enter height of triangle :'))
        a=0.5*base*height
        print(f'Area of triangle is :{a:.2f}')
    case 3:
        dim1=float(input('Enter dim1 of rectangle :'))
        dim2=float(input('Enter dim2 of rectangle :'))
        a=dim1*dim2
        print(f'Area of rectangle is :{a:.2f}')
    case 4:
        print('Thanks for using this application')
    case _:
        print('Invalid Option please enter from (1-4)')