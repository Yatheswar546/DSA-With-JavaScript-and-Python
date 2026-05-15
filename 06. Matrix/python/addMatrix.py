# Problem Description:

# Add two matrices and create a new matrix and also print the new resultant matrix in matrix representation


def addMatrix(matrix1, matrix2):

    r1 = len(matrix1)
    c1 = len(matrix1[0])

    r2 = len(matrix2)
    c2 = len(matrix2[0])

    if(r1!=r2 or c1!=c2):
        print("Addition of these two matrices are not possible")
        return;

    result_matrix = []

    for i in range(r1):
        row = []
        for j in range(c1):
            sum = matrix1[i][j] + matrix2[i][j]
            row.append(sum)
        result_matrix.append(row)

    
    for i in range(r1):
        for j in range(c1):
            print(result_matrix[i][j], end=" ")
        print()

print("Enter your first matrix row by row (press Enter on a blank line to finish):")

matrix1 = []
while True:
    line = input()
    if not line.strip():  # Stops reading if the user enters a blank line
        break
    
    # Split the line by spaces, convert each string to an integer, and create a list
    row = [int(x) for x in line.split()]
    matrix1.append(row)


print("Enter your second matrix row by row (press Enter on a blank line to finish):")

matrix2 = []
while True:
    line = input()
    if not line.strip():  # Stops reading if the user enters a blank line
        break
    
    # Split the line by spaces, convert each string to an integer, and create a list
    row = [int(x) for x in line.split()]
    matrix2.append(row)

addMatrix(matrix1, matrix2);

# Time Complexity  : O(r1 * c1)
# Space Complexity : O(r1 * c1)