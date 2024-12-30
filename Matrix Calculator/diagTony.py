import numpy as np

def input_matrix():
    """Prompt the user to input a square matrix."""
    while True:
        try:
            n = int(input("Enter the size of the square matrix (n x n): "))
            print("Enter the matrix row by row (space-separated values):")
            matrix = []
            for _ in range(n):
                row = list(map(float, input().strip().split()))
                if len(row) != n:
                    raise ValueError("Each row must have exactly n values.")
                matrix.append(row)
            return np.array(matrix)
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def calculate_eigen(matrix):
    """Calculate the eigenvalues and eigenvectors of a matrix."""
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

def check_diagonalizability(matrix):
    """Check if a matrix is diagonalizable."""
    eigenvalues, eigenvectors = calculate_eigen(matrix)
    unique_eigenvalues = set(eigenvalues)

    for eigenvalue in unique_eigenvalues:
        algebraic_multiplicity = np.count_nonzero(np.isclose(eigenvalues, eigenvalue))
        geometric_multiplicity = np.linalg.matrix_rank(
            eigenvectors[:, np.isclose(eigenvalues, eigenvalue)]
        )

        if algebraic_multiplicity != geometric_multiplicity:
            return False, eigenvalues, eigenvectors

    return True, eigenvalues, eigenvectors

def main():
    """Main function to interact with the user."""
    print("Diagonalizable Matrix Checker")
    matrix = input_matrix()
    is_diagonalizable, eigenvalues, eigenvectors = check_diagonalizability(matrix)

    print("\nMatrix:")
    print(matrix)
    print("\nEigenvalues:")
    print(eigenvalues)
    print("\nEigenvectors:")
    print(eigenvectors)

    if is_diagonalizable:
        print("\nThe matrix is diagonalizable.")
    else:
        print("\nThe matrix is not diagonalizable.")