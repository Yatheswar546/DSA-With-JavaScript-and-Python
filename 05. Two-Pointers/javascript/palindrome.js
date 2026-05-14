// Problem Description
// Given a string comprising only lowercase alphabets, determine whether it qualifies as a palindrome.

// A string is considered a palindrome if it reads the same forwards and backwards.

// Note:

// For the purpose of this problem, we define empty string as valid palindrome.

// Input format
// The only line contains a string.

// Output format
// True or False.

// Sample Input 1
// madam

// Sample Output 1
// true

// Explanation
// "madam" spelt backwards is "madam", therefore, it is a palindrome.

// Sample Input 2
// crio

// Sample Output 2
// false

// Explanation
// "crio" spelt backwards is "oirc", therefore, it is not a palindrome.

// Constraints
// 1 <= s.length <= 2 * 10^5

function checkPalindrome(str) {

    let leftPtr = 0;
    let rightPtr = str.length-1;

    while(leftPtr < rightPtr) {
        if(str[leftPtr] != str[rightPtr]) {
            return false 
        }

        leftPtr++;
        rightPtr--;
    }

    return true

}

/* 
    Time Complexity  : O(n)
    Space Complexity : O(1)
*/