for num in range(1,101):
  if num%2==0:
    continue
  print(num,end='')

print()
num=1
while num<=100:
  if num%2!=0:
    num=num+1
    continue
  print(num,end='')
  num=num+1