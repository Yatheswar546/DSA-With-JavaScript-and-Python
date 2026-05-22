// Problem Description

// Implement the function stringCompression() that:
// Accepts a string s as an argument
// Returns
// a compressed string for each group of consecutive repeated characters by replacing the group with the character followed by the number of occurrences.
// the original string if the compressed string is not shorter than the original string

// Note
// You can assume the string contains only uppercase and lowercase letters (a-z).

// Input Format
// A single line containing the string s.

// Output Format
// A single line representing the compressed string as specified. If compression does not reduce the size, return the original string.

// Sample Input 1
// aabccccc

// Sample Output 1
// a2b1c5

// Explanation 1
// First 'a' repeats two times, then 'b' repeats once, then 'c' repeats two times.

// Constraints
// 1 <= length(S) <= 100000

// Code

let s = 'aabbbbccccd'
let n = s.length

let count = 1
let finalString = ''

for(let i=1; i<n; i++) {
    
    if(s[i] == s[i-1]) {
        count++;
    }
    
    else if(s[i] != s[i-1]) {
        finalString += s[i-1]
        finalString += count
        count = 1
    }
}

finalString += s[n-1]
finalString += count

console.log(finalString)

/* 
    Time Complexity  : O(n)
    Space Complexity : O(n)
*/