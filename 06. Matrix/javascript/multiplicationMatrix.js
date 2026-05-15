// Problem Description:

// Multiply two matrices and create a new matrix and also print the new resultant matrix in matrix representation

function multiplyMatrix(matrix1, matrix2) {

    let r1 = matrix1.length;
    let c1 = matrix1[0].length;

    let r2 = matrix2.length;
    let c2 = matrix2[0].length;

    if(c1 !== r2) {
        console.log("Multiplication for these matrices is not possible");
        return;
    }

    let result_matrix = [];

    for(let i=0; i<r1; i++) {
        let row = []
        
        for(let j=0; j<c2; j++) {
            let sum = 0

            for(let k=0; k<c1; k++) {
                sum += matrix1[i][k] * matrix2[k][j];
            }
            row.push(sum)
        }
        result_matrix.push(row);
    }
    
    for(let i=0; i<r1; i++) {
        let rowString = " ";
        for(let j=0; j<c2; j++) {
            rowString += result_matrix[i][j] + " ";
        }
        console.log(rowString);
    }
}

multiplyMatrix(([[1,2,3], [4,5,6]]), ([[1,2], [3,4], [5,6]]));


/*
    Time Complexity  : O(r1 * c2 * c1)
    Space Complexity : O(r1 * c2)
*/