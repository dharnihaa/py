no_of_elements = int(input('Enter the size of list: '))
array =[]
#Read Array elements
print( 'Enter the elements of the list: ')
for i in range(0,no_of_elements,1):
 element=input()
 array.append(int(element))
#finding the first three numbers
max1=0
max2=0
max3=0
for i in range(0,no_of_elements,1):
 if array[i] >max1:
  max3 = max2
  max2=max1
  max1=array[i]
 elif array[i] >max2:
  max3=max2
  max2=array[i]
 elif array[i] >max3:
  max3=array[i]

#Display the largest elements
print( 'Max1:{}'.format(max1))
print( 'Max2:{}'.format(max2))
print( 'Max3:{}'.format(max3))
