// Problem Description:

// Find the sum of diagonal elements of a matrix

function diagonalSum(matrix) {

    let row = matrix.length;
    let col = matrix[0].length;

    let sum = 0
    for(let i=0, j=0; i<row; i++, j++) {
        if(i==j) {
            sum += matrix[i][j];
        }
    }

    return sum;

}

console.log(diagonalSum([[1,2,3], [4,5,6], [7,8,9]]))