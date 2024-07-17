class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_row = []
        zero_column = []
        n = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row.append(i)
                    zero_column.append(j)
                    
        for i in zero_row:
            for j in range(n):
                matrix[i][j] = 0

        for i in range(len(matrix)):
            for j in zero_column:
                matrix[i][j] = 0
        print(matrix)