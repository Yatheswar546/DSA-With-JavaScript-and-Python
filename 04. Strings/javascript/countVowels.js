// Description
// Assessment
// Problem Description
// Given a string, count the total number of vowels present in that string.

// Input format
// First line contains the given string.

// Output format
// Print the total number of vowels.

// Sample Input 1
// language

// Sample Output 1
// 4

// Explanation
// There are total 4 vowels in the string "language" i.e. 'a', 'u', 'a', 'e'.

// Constraints
// 0 < Length of string < 100

function countVowels(str) {

    let count = 0
    let vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"];

    for(let i=0; i < str.length; i++) {
        if(vowels.includes(str[i])) {
            count++;
        }    
    }

    return count;

}

/* 
    Time Complexity  : O(n)
    Space Complexity : O(1)
    the vowels array size is fixed (10 elements only)
    fixed size space is considered constant space
*/