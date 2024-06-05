def matrix_multiplication(A, B):
  if len(A[0]) != len(B):
      return None  
  result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        result[i][j] += A[i][k] * B[k][j]
    return result

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

product = matrix_multiplication(A, B)
if product is None:
    print("Cannot multiply the matrices: number of columns in A is not equal to number of rows in B.")
else:
    print("Product of the matrices:")
    for row in product:
        print(row)
