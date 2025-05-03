def power():
  num=5 
  def find_power(p):
    res=num**p
    return res
  return find_power


find_power=power()
res1=find_power(2)
res2=find_power(3)
res3=find_power(4)
print(res1,res2,res3)
