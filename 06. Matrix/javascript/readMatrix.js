// Problem Description:

// Access and print matrix elements in same matrix representation.

function readMatrix(matrix) {

    let row = matrix.length;
    let col = matrix[0].length;

    for(let i=0; i<row; i++) {
        let rowString = "";
        for(let j=0; j<col; j++) {
            rowString += matrix[i][j] + " ";
        }
        console.log(rowString);
    }
}

readMatrix([[1,2,3], [4,5,6], [7,8,9]])

/* 
    Time Complexity : O(n*m)
    Space Complexity : O(1)
*/