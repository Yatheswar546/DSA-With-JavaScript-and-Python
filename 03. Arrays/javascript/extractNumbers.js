// Problem Description
// Implement the function extractNumbers() that

// Accepts two arguments a number N and an array arr containing a mix of strings and numbers (in string type)

// Returns a new array that retains only the numbers present in the original array in the same order.

// Example: from the provided array arr = [a, 1, b, 2, c, d, 3, 4, e], the output array should contain [1, 2, 3, 4]. The numbers in the original array can be single or multiple digits, and there may be strings interspersed among them.

// Note
// The numbers in the array are also of string type.

// The order of integers in the input array must be maintained.

// Input format
// First line is an integer N: the number of elements in the input array Second line is arr: the elements of the input array

// Output format
// Return the expected integer array.

// Sample Input 1
// 8

// a 3 long 17 crio dsa 100 20

// Sample Output 1
// 3 17 100 20

// Explanation
// The input array contains four integers [3, 17, 100, 20]

// Constraints
// 1 <= N <= 10^5

// 1 <= |arr[i]| <= 8 where |arr[i]| is the length of the string

// Code 

function extractNumbers(arr, n) {

    let resultArray = [];

    for(let i=0; i<n; i++) {
        
        if(Number.isInteger(arr[i])) {
            resultArray.push(arr[i]);
        }

    }

    return resultArray;

}