number=int(input("Enter number"))
trails=10
approx = 0.5*number
for i in range(trails):
  better =0.5*(approx+number/approx)
  approx=better
print(better)