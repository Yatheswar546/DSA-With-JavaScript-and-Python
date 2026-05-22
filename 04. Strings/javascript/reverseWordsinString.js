// Problem Description:

// A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

// Return a string of the words in reverse order concatenated by a single space.

// Note that s may contain leading or trailing spaces or multiple spaces between two words.

// The returned string should only have a single space separating the words.

// Do not include any extra spaces.

// Input format
// String s.

// Output format
// The function should return a string of the words in reverse order concatenated by a single space.

// Sample Input 1
// hello world

// Sample Output 1
// world hello

// Explanation
// The given words after being reversed gives:world hello

// Your reversed string should not contain leading or trailing spaces.

// Constraints
// 1 <= s.length <= 10^5

// s contains English letters (upper-case and lower-case), digits, and spaces ' '.

// There is at least one word in s.

// Code:

let s = "  hello   world   ";
let n = s.length;

let word = ''
let finalString = ''

for(let i=n-1; i>=0; i--){
    
    if(s[i] == ' ') {
        continue;
    } 
    
    else {
      while(i>=0 && s[i] != ' ') {
          word += s[i];
          i--;
      }
        
      for(let j=word.length-1; j>=0; j--) {
          finalString += word[j];
      }
      
      while(i>=0 && s[i]==' ') {
          i--;
      }
      
      if(i>=0) {
          finalString+=' '
      }
      word = ''
      
      i++
        
    }
}

console.log(finalString);

/*
    Time Complexity  : O(n)
    Space Complexity : O(n)
*/