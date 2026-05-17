# Leetcode Problem - 566

# Problem Description:

# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

# Example 1:
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]

# Example 2:
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]

# Code:

def reShapeMatrix(mat, r, c):

    n = len(mat)
    m = len(mat[0])

    if( n*m != r*c):
        return mat

    resMatrix = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(n):
        for j in range(m):

            index = i * m + j

            newRow = index // c
            newCol = index % c

            resMatrix[newRow][newCol] = mat[i][j]

    return resMatrix

print(reShapeMatrix([[1,2,3],[4,5,6]], 3, 2));