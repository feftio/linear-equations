from linear import linear
import numpy as np

matrix_right = [
    [2, 4, 6],
    [8, 1, 3],
    [5, 7, 9]
]

matrix_wrong = [
    [1, 1, -2],
    [2, 3, -7],
    [5, 2, 1]
]

answer = [6, 16, 16]

# print(np.linalg.solve(matrix_right, answer))
# print(np.linalg.solve(matrix_wrong, answer))
# print(linear(matrix_right, answer))
# print(linear(matrix_wrong, answer))