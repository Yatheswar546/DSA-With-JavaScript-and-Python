// Problem Description
// You are given a array of numbers. Your task is to rotate the given array left(anti-clockwise) by n units from the starting index. You are required to return the rotated array.

// Input format
// First line contains an integer n, the size of the array and k the number of rotations. 
// Second line contains n integers, the elements of the array.

// Output format
// Return the rotated string.

// Sample Input 1
// 5 1
// 1 2 3 4 5

// Sample Output 1
// 2 3 4 5 1

// Explanation
// In the left rotation, the subarray of length 1 from the beginning is [1], this subarray is removed from the beginning and attached to the end of the array(i.e. anti-clockwise).

// Sample Input 2
// 5 2
// 1 2 3 4 5

// Sample Output 2
// 3 4 5 1 2

// Constraints
// 1 <= n <= 10^5 1 <= arr[i] <= 10^5

// Code 
function leftRotate(arr, k) {
    
    let resultArray = []
    let n = arr.length;

    let k = k%n;

    for(i=k; i<n; i++) {
        resultArray.push(arr[i]);
    }

    for(i=0; i<k; i++){
        resultArray.push(arr[i]);
    }

    return resultArray;

}

// Code for Right rotation
function rightRotate(arr, k) {

    let resultArray = [];
    let n = arr.length;

    k = k%n; 
    
    for(i=n-k; i<n; i++) {
        resultArray.push(arr[i]);
    }

    for(i=0; i<n-k; i++) {
        resultArray.push(arr[i]);
    }

    return resultArray
}

/*  
    For both cases:
    Time Complexity = O(n)
    Space Complexity = O(n) + O(1)
*/