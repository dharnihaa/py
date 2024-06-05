def hcf(a,b):
 if(b==0):
  return a
 else:
  return hcf(b,a%b)
a=int(input("Enter no 1 : "))
b=int(input("Enter no 2 : "))
print(hcf(a,b))