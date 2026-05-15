# Problem Description:

# Access and print matrix elements in same matrix representation.

def readMatrix(matrix):

    row = len(matrix)
    col = len(matrix[0])

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

readMatrix(matrix);

# Time Complexity : O(n*m)
# Space Complexity : O(1)