# Problem Description:

# Find the sum of diagonal elements of a matrix

def diagonalSum(matrix):

    n = len(matrix)

    sum = 0
    for i,j in zip(range(n), range(n)):

        if(i==j):
            sum += matrix[i][j]

    return sum


print("Enter your matrix row by row (press Enter on a blank line to finish):")

matrix = []
while True:
    line = input()
    if not line.strip():  # Stops reading if the user enters a blank line
        break
    
    # Split the line by spaces, convert each string to an integer, and create a list
    row = [int(x) for x in line.split()]
    matrix.append(row)

print(diagonalSum(matrix));

# Time Complexity  : O(n)
# Space Complexity : O(1)