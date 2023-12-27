import numpy as np

# Creating a matrix
A = np.array([[4, -2], [1, 1]])

# Calculating eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
