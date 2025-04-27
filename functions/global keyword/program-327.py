# Program to find area of triangle

base=0.0 # Global Variable
height=0.0 # Global Variable

def read():
    global base,height
    base=float(input("Enter Base of Triangle :"))
    height=float(input("Enter Height of Triangle :"))

def find_area():
    area=0.5*base*height
    print(f'Area of triangle is {area:.2f}')

read()
find_area()
