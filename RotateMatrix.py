from typing import List


class RotateMatrixFirstSolution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        # consider all squares one by one
        for x in range(0, int(N//2)):
            # consider elements in groups of 4 in the current square
            for y in range(x, N-1-x):
                # store current cell in temp variable
                temp = matrix[x][y]

                # you need to overwrite them in proper order so that the values are not                       missing

                # move values from bottom left to top left
                matrix[x][y] = matrix[N-1-y][x]

                # move values from bottom right to bottom left
                matrix[N-1-y][x] = matrix[N-1-x][N-1-y]

                # move values from top right to bottom right
                matrix[N-1-x][N-1-y] = matrix[y][N-1-x]

                # move values from top left to top right
                matrix[y][N-1-x] = temp


# Solution
s = RotateMatrixFirstSolution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.rotate(matrix)
print(matrix)


class RotateMatrixSecondSolution():
    def rotate(self, matrix: List[List[int]]) -> None:
        pass
