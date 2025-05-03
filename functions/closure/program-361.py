def power(num):
  def find_power(p):
    res=num**p
    return res
  return find_power

power5=power(5)
power6=power(6)
power9=power(9)
r1=power5(2)
r2=power6(3)
r3=power9(2)
print(r1,r2,r3)
r4=power5(3)
print(r4)
