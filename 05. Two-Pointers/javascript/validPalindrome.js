// LeetCode - Problem 9

// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

// Given a string s, return true if it is a palindrome, or false otherwise.

// Example 1:

// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.
// Example 2:

// Input: s = "race a car"
// Output: false
// Explanation: "raceacar" is not a palindrome.
// Example 3:

// Input: s = " "
// Output: true
// Explanation: s is an empty string "" after removing non-alphanumeric characters.
// Since an empty string reads the same forward and backward, it is a palindrome.
 

// Constraints:

// 1 <= s.length <= 2 * 105
// s consists only of printable ASCII characters.
 

// 1st Approach

function isPalindrome(s) {
    lowerCaseStr = s.toLowerCase()
    
    let newStr = ""

    for(let i=0; i<lowerCaseStr.length; i++) {
        if((lowerCaseStr[i] >= 'a' && lowerCaseStr[i] <= 'z') || 
            (lowerCaseStr[i] >= '0' && lowerCaseStr[i] <= '9')) {
            newStr += lowerCaseStr[i]
        }
    }
    
    let leftPtr = 0;
    let rightPtr = newStr.length - 1;
    
    while(leftPtr < rightPtr) {

        if(newStr[leftPtr] != newStr[rightPtr]) {
            return false
        }
        
        leftPtr++;
        rightPtr--;
    }
    
    return true

};

/* 
    Time Complexity  : O(n)
    Space Complexity : O(n)
*/

// 2nd Approach
function isPalindrome(s) {
    
    const isAlphanumeric = str => /^[a-z0-9]+$/i.test(str);
    
    lowerCaseStr = s.toLowerCase()
    
    let leftPtr = 0;
    let rightPtr = lowerCaseStr.length - 1;
    
    while(leftPtr < rightPtr){
        
        let i = lowerCaseStr[leftPtr];
        let j = lowerCaseStr[rightPtr];

        if(isAlphanumeric(i) && isAlphanumeric(j)) {
            if(i != j) {
                return false
            }
            leftPtr++;
            rightPtr--
        }
        else if(!isAlphanumeric(i)) {
            leftPtr++
        }
        else if(!isAlphanumeric(j)) {
            rightPtr--
        }

    }
    
    return true
}

/* 
    Time Complexity  : O(n)
    Space Complexity : O(1)
*/