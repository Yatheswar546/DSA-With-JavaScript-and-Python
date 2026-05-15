# Problem Description:

# Find the sum of non-diagonal elements of a matrix

print("Enter your matrix row by row (press Enter on a blank line to finish):")

def nonDiagonalSum(matrix):

    n = len(matrix)

    sum = 0
    for i in range(n):

        sum += matrix[i][n - 1 -i]

    return sum


matrix = []
while True:
    line = input()
    if not line.strip():  # Stops reading if the user enters a blank line
        break
    
    # Split the line by spaces, convert each string to an integer, and create a list
    row = [int(x) for x in line.split()]
    matrix.append(row)

print(nonDiagonalSum(matrix));

# Time Complexity  : O(n)
# Space Complexity : O(1)