// Problem Description:

// Tranpose the below matrix 

// function transposeMatrix(matrix) {

//     let row = matrix.length;
//     let col = matrix[0].length;

//     // create a zero matrix 
//     let transpose_Matrix = Array.from({ length: col}, () => Array(row).fill(0));

//     for(let i=0; i<row; i++) {
//         for(let j=0; j<col; j++) {
//             // console.log(j,i + " and " + i,j)
//             transpose_Matrix[j][i] = matrix[i][j];
//         }
//     }

//     for(let i=0; i<col; i++) {
//         let rowString = "";

//         for(let j=0; j<row; j++) {
//             rowString += transpose_Matrix[i][j] + " ";
//         }
//         console.log(rowString)
//     }

// }

// transposeMatrix([[1,2,3], [4,5,6]])


/* 
    Time Complexity  : O(row * col)
    Space Complexity : O(row * col)
*/


// 2nd Approach:
// Without creating a new Matrix, but IT IS POSSIBLE only for Matrix(n * n)

function transposeMatrix(matrix) {

    let row = matrix.length;
    let col = matrix[0].length;

    for(let i=0; i<row; i++) {
        for(let j=i+1; j<col; j++) {

            let temp = matrix[i][j];
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp;
        }
    }

    for(let i=0; i<col; i++) {
        let rowString = "";

        for(let j=0; j<row; j++) {
            rowString += matrix[i][j] + " ";
        }
        console.log(rowString)
    }

}

transposeMatrix([[1,2,3], [4,5,6], [7,8,9]])

/* 
    Time Complexity  : O(row * col)
    Space Complexity : O(1)
*/