// Leetcode Problem: 54

// Given an m x n matrix, return all elements of the matrix in spiral order.

// Example 1:
// Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [1,2,3,6,9,8,7,4,5]

// Example 2:
// Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
// Output: [1,2,3,4,8,12,11,10,9,5,6,7]

var spiralOrder = function(matrix) {
    
    let m = matrix.length;
    let n = matrix[0].length;

    let top = 0;
    let bottom = m-1;
    let left = 0;
    let right = n-1;

    let res = [];

    while(top<=bottom && left<=right) {

        for(let i=left; i<=right; i++) {
            res.push(matrix[top][i]);
        }
        top++;

        for(let i=top; i<=bottom; i++) {
            res.push(matrix[i][right]);
        }
        right--;

        if(top<=bottom) {
            for(let i=right; i>=left; i--) {
                res.push(matrix[bottom][i]);
            }
        }
        bottom--;

        if(left<=right) {
            for(let i=bottom; i>=top; i--) {
                res.push(matrix[i][left]);
            }
        }
        left++;
        
    }

    return res;

};

/*
    Time Complexity  : O(m × n)
    Space Complexity : O(m × n)
*/