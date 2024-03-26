import numpy as np

# Set 1: Coefficient matrix A and constant vector b
A1 = np.array([[3, -1, 1],
               [3, 6, 2],
               [3, 3, 7]])
b1 = np.array([1, 0, 4])

# Set 2: Coefficient matrix A and constant vector b
A2 = np.array([[10, -1, 0],
               [-1, 10, -2],
               [0, -2, 10]])
b2 = np.array([9, 7, 6])

# Set 3: Coefficient matrix A and constant vector b
A3 = np.array([[10, 5, 0, 0],
               [5, 10, -4, 0],
               [0, -4, 8, -1],
               [0, 0, -1, 5]])
b3 = np.array([6, 25, -11, -11])

# Set 4: Coefficient matrix A and constant vector b
A4 = np.array([[4, 1, 1, 0, 1],
               [-1, -3, 1, 1, 0],
               [2, 1, 5, -1, -1],
               [-1, -1, -1, 4, 0],
               [0, 2, -1, 1, 4]])
b4 = np.array([6, 6, 6, 6, 6])

# Solve the systems of linear equations
x1 = np.linalg.solve(A1, b1)
x2 = np.linalg.solve(A2, b2)
x3 = np.linalg.solve(A3, b3)
x4 = np.linalg.solve(A4, b4)

# Print the solutions
print("Solution for set 1:")
print(x1)
print("\nSolution for set 2:")
print(x2)
print("\nSolution for set 3:")
print(x3)
print("\nSolution for set 4:")
print(x4)
