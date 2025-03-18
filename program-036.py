# Write a program to find input year is leap year or not

year=int(input('Enter any year :'))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f'{year} is leap year :')
        else:
            print(f'{year} is not leap year :')
    else:
        print(f'{year} is leap year :')
else:
    print(f'{year} is not leap year :')