// Problem Description
// Write a program that reverses a string.

// Input format
// First line will be a single string

// Output format
// 1<=size(S)<=200000

// Sample Input 1
// abc

// Sample Output 1
// cba

// Explanation
// cba is reverse of abc.

// Sample Input 2
// aaa

// Sample Output 2
// aaa

// Explanation
// aaa is reverse of aaa.

// Constraints
// Print the reverse of the string in a single line.

function reverseString(str) {

    let arr = str.split("");

    let leftPtr = 0;
    let rightPtr = arr.length - 1;

    while(leftPtr < rightPtr) {

        let temp = arr[leftPtr];
        arr[leftPtr] = arr[rightPtr];
        arr[rightPtr] = temp;

        leftPtr++;
        rightPtr--;

    }

    return arr.join("");

}

/*
    Time Complexity  - O(n)
    Space Complexity - O(n)
*/