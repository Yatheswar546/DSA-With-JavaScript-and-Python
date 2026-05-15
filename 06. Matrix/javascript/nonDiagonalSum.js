// Problem Description:

// Find the sum of non-diagonal elements of a matrix

function diagonalSum(matrix) {

    let row = matrix.length;
    let col = matrix[0].length;
    
    let sum = 0
    for(let i=0; i<row; i++) {
            sum += matrix[i][row-1-i];
        }

    return sum;

}

console.log(diagonalSum([[1,2,2], [4,5,6], [7,8,9]]))

/*  
    Time Complexity  : O(n)
    Space Complexity : O(1)
*/