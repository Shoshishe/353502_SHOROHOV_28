import numpy as np


class MatrixCalculator:
    @staticmethod
    def GenerateNewMatrix(arr: np.array) -> np.array:
        max_val = np.max(arr)
        return np.divide(arr, max_val)

    @staticmethod
    def CreateMatrix(n, m) -> np.array:
        return np.random.random((n, m))


def solve_task_5():
    matrix = (MatrixCalculator.CreateMatrix(4, 5))
    print("Matrix, generated randomly: " + str(matrix))
    matrix /= matrix.max()
    print("Matrix changed by dividing: " + str(matrix))


def main():
    solve_task_5()


if __name__ == "__main__":
    main()
