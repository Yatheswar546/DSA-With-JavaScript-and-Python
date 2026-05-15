# Problem Description:

# Multiply two matrices and create a new matrix and also print the new resultant matrix in matrix representation

def multiplyMatrix(matrix1, matrix2):

    r1 = len(matrix1)
    c1 = len(matrix1[0])

    r2 = len(matrix2)
    c2 = len(matrix2[0])

    if(c1 != r2):
        print("Multiplication of these two matrices are not possible")
        return;

    result_matrix = []

    for i in range(r1):
        row = []
        for j in range(c2):
            sum = 0
            for k in range(c1):
                sum += (matrix1[i][k] * matrix2[k][j])
            row.append(sum)
        result_matrix.append(row)

    for i in range(r1):
        for j in range(c2):
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

multiplyMatrix(matrix1, matrix2);

# Time Complexity  : O(r1 * c2 * c1)
# Space Complexity : O(r1 * c2)