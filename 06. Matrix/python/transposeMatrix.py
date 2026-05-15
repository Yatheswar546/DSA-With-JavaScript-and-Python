# Problem Description:

# Transpose the below matrix 

# def transposeMatrix(matrix):

#     row = len(matrix)
#     col = len(matrix[0])

#     # create a zero matrix 
#     transpose_matrix = [[0 for _ in range(row)] for _ in range(col)]

#     for i in range(row):
#         for j in range(col):
#             transpose_matrix[j][i] = matrix[i][j];

#     for i in range(col):
#         for j in range(row):
#             print(transpose_matrix[i][j], end=" ")
#         print()


# print("Enter your matrix row by row (press Enter on a blank line to finish):")

# matrix = []
# while True:
#     line = input()
#     if not line.strip():  # Stops reading if the user enters a blank line
#         break
    
#     # Split the line by spaces, convert each string to an integer, and create a list
#     row = [int(x) for x in line.split()]
#     matrix.append(row)

# transposeMatrix(matrix);

# Time Complexity  : O(row * col)
# Space Complexity : O(row * col)

###############################################################################

# 2nd Approach:
# Without creating a new Matrix, but IT IS POSSIBLE only for Matrix(n * n)

def transposeMatrix(matrix):

    row = len(matrix)
    col = len(matrix[0])
    
    for i in range(row):
        for j in range(i+1, col):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=" ")
        print()

print("Enter your matrix row by row (press Enter on a blank line to finish):")

matrix = []
while True:
    line = input()
    if not line.strip():  # Stops reading if the user enters a blank line
        break
    
    # Split the line by spaces, convert each string to an integer, and create a list
    row = [int(x) for x in line.split()]
    matrix.append(row)

transposeMatrix(matrix);

# Time Complexity  : O(row * col)
# Space Complexity : O(1)