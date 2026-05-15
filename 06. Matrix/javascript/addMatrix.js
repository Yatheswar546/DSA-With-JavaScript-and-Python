// Problem Description:

// Add two matrices and create a new matrix and also print the new resultant matrix in matrix representation

function addMatrix(matrix1, matrix2) {

    let n1 = matrix1.length;
    let m1 = matrix1[0].length;

    let n2 = matrix2.length;
    let m2 = matrix2[0].length;

    if(n1 !== m1 || n2 !== m2) {
        console.log("Matrix Addition is not possible for these matrices");
        return;
    }
    
    let result_matrix = [];

    for(let i=0; i<n1; i++) {
        let row = [];            
        for(let j=0; j<m1; j++) {
            let sum = matrix1[i][j] + matrix2[i][j];
            row.push(sum); 
        }
        result_matrix.push(row);
    }

    for(let i=0; i<n2; i++) {
        let rowString = ""
        for(let j=0; j<m2; j++) {
            rowString += result_matrix[i][j] + " ";
        }
        console.log(rowString);
    } 

}

addMatrix(([[1,2,3], [4,5,6], [7,8,9]]), ([[1,2,3], [4,5,6], [7,8,9]]));

/*
    Time Complexity  : O(n*m)
    Space Complexity : O(n*m)
*/