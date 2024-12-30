import numpy as np

def create_matrix(rowsize, columnsize):
  matrix = []

  for i in range(rowsize):
    row = []

    for j in range(columnsize):
      try:
        nums = int(input(f"Enter the value at index ({i}, {j}) (one at a time): "))
        row.append(nums)
      except:
        return

    matrix.append(row)

  return np.array(matrix)

def SVD_function(matrix):
  U, S, Vtranspose = np.linalg.svd(matrix)
  return U, S, Vtranspose

def main():
  rowsize = int(input('Enter the Row size: '))
  columnsize = int(input('Enter the Column size: '))

  matrix = create_matrix(rowsize, columnsize)

  print("\nInputted Matrix: ")
  print(matrix)
  print("\n")

  U, S, Vtranspose = SVD_function(matrix)
  print("Matrix U :")
  print(U)
  print("\n")

  print("Matrix Σ :")
  S_final = np.zeros((matrix.shape[0], matrix.shape[1]))
  np.fill_diagonal(S_final, S)
  print(S_final)
  print("\n")

  print("Vᵀ (Right Singular Vectors):")
  print(Vtranspose)
  print("\n")

  print("Result check: ")
  result_check = U @ S_final @ Vtranspose
  print(result_check)