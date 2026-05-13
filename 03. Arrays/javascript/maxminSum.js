// Problem Description
// Given an array of integers, write a program to find the sum of the minimum and maximum values of the array.

// Input format
// First line contains an integer N, the size of the array

// Second line contains the integers present in the array

// Output format
// Return expected integer

// Sample Input 1
// 5

// 10 15 4 5 19

// Sample Output 1
// 23

// Explanation
// The minimum and maximum values of the array are 4 and 19 respectively, totaling 23

// Sample Input 2
// 3

// 10 10 10

// Sample Output 2
// 20

// Explanation
// The minimum and maximum values of the array are the same, i.e, 10, totaling 20

// Constraints
// 1 <= N <= 10^5

// 1 <= arr[i] <= 10^9

function maxminSum(arr) {

    let n = arr.length;

    let min = arr[0]
    let max = arr[0];

    for(let i=0; i<n; i++) {
        if(arr[i] > max) {
            max = arr[i];
        }
        if(arr[i] < min) {
            min = arr[i]
        }
    }

    let result = max + min;

    return result;

}

/*
    Time Complexity - O(n)
    Space Complexity - O(1)
*/