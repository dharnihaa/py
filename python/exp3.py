def power(base,exp):
  result=1
  
  for i in range(exp):
    result*=base
  return result
base=int(input("Enter num "))
exp=int(input("Enter num "))
print(power(base,exp))