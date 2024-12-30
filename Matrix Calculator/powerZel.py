import numpy as np

def power_method(matrix, max_iterations=10, tolerance=0.01):
    
    n = matrix.shape[0]

    eigenvector = np.ones(n)
    eigenvalue = 0

    for i in range(max_iterations):
       
        new_vector = np.dot(matrix, eigenvector)

        new_vector_norm = np.linalg.norm(new_vector)
        new_eigenvector = new_vector / new_vector_norm
  
        new_eigenvalue = np.dot(new_eigenvector, np.dot(matrix, new_eigenvector))
      
        if np.abs(new_eigenvalue - eigenvalue) < tolerance:
            return new_eigenvalue, new_eigenvector

        eigenvector = new_eigenvector
        eigenvalue = new_eigenvalue

    return eigenvalue, eigenvector

def main():
    print("Power Method Application for Dominant Eigenvalue")
    
    n = int(input("Enter the size of the matrix (n x n): "))
    print("Enter the matrix elements row by row:")
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            print("The matrix must be square")
            return
        matrix.append(row)
    matrix = np.array(matrix)

    eigenvalue, eigenvector = power_method(matrix)

    print("\nResults:")
    print(f"Dominant Eigenvalue: {eigenvalue:.6f}")
    print("Dominant Eigenvector:")
    print(eigenvector)

