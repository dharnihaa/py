def linear_search(arr,target):
  for index, element in enumerate(arr):
    if element==target:
       return index
  return -1
arr=[10, 20, 30, 67]
target=int(input("enter target "))
print(linear_search(arr,target))