import numpy as np

def input_matrix():
    """Prompts the user to input a square matrix and validates the input."""
    while True:
        try:
            # Input dan validasi ukuran matriks
            size = int(input("Enter the size of the square matrix (n x n): "))
            if size <= 0:  # Validasi ukuran matriks
                raise ValueError("The size of the matrix must be greater than 0.")
            
            print("Enter the matrix row by row, values separated by spaces:")
            matrix = []
            for i in range(size):
                row = list(map(float, input(f"Row {i + 1}: ").split()))
                if len(row) != size:
                    raise ValueError("Each row must have exactly n elements.")
                matrix.append(row)
            
            return np.array(matrix)
        
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def lu_decomposition(matrix):
    """Performs LU decomposition using Doolittle's method."""
    n = matrix.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Upper Triangular
        for k in range(i, n):
            sum_u = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = matrix[i][k] - sum_u

        # Lower Triangular
        for k in range(i, n):
            if i == k:
                L[i][i] = 1  # Diagonal as 1
            else:
                sum_l = sum(L[k][j] * U[j][i] for j in range(i))
                if U[i][i] == 0:
                    raise ValueError("Matrix is singular and cannot be decomposed.")
                L[k][i] = (matrix[k][i] - sum_l) / U[i][i]

    return L, U

def main():
    print("LU Decomposition Application")
    print("===========================")

    try:
        matrix = input_matrix()
        print("\nInput Matrix:")
        print(matrix)

        L, U = lu_decomposition(matrix)

        print("\nLower Triangular Matrix L:")
        print(L)

        print("\nUpper Triangular Matrix U:")
        print(U)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
