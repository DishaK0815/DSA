class Solution:
    def Set_matrix_zero(self, matrix):
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        row_zero = any(matrix[0][j] == 0 for j in range(cols))
        col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Mark rows and columns to be zeroed
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Zero out cells based on marks
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero out first column if needed
        if col_zero:
            for i in range(rows):
                matrix[i][0] = 0

        return matrix

# Test
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol = Solution()
print(sol.Set_matrix_zero(matrix))



class solution:
    def set_matrix_zero_brute(self, matrix):
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])
        zero_positions = []

        # Find all zero positions
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))

        # Set rows and columns to zero
        for i, j in zero_positions:
            for col in range(cols):
                matrix[i][col] = 0
            for row in range(rows):
                matrix[row][j] = 0

        return matrix
    
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol = solution()
print(sol.Set_matrix_zero_brute(matrix))