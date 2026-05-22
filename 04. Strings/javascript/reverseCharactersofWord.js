// Problem Description
// Write a program to reverse the words present in a sentence.

// Input format
// First line contains an string consisting of words separated by spaces.

// Output format
// Return the string with it's words reversed.

// Sample Input 1
// abc def ghi

// Sample Output 1
// cba fed ihg

// Explanation
// abc reversed is cba, def reversed is fed, ghi reversed is igh.

// Constraints
// 1 <= str.length <= 10^5

let s = 'abc def ghi'
let n = s.length

let finalString = ''
let word = ''

for(let i=0; i<n; i++) {
    
    if(s[i] != ' ') {
        word += s[i]
    }
    
    else if((i==n-1) || (s[i] == ' ')) {
        for(let j=word.length-1; j>=0; j--) {
            finalString += word[j];
        }
        word = ''
        finalString += ' '
    }
}

for(let j=word.length-1; j>=0; j--) {
    finalString += word[j];
}

console.log(finalString)

/*
    Time Complexity  : O(n)
    Space Complexity : O(n)
*/