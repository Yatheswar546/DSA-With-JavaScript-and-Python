/*
Problem Description: Check if the given string is palindrome or not

Input  : ababa
Output : true

Input  : ababc
Output : false

Input  : abcba
Output : true
*/

// 1st Approach:
function isPalindrome(str) {

    if(str.length <= 1) {
        return str;
    }

    return isPalindrome(str.substring(1)) + str[0];

}

let str = "ababa";
let reversedStr = isPalindrome(str);


if(str === reversedStr) {
    console.log("true");
}

else {
    console.log("false");
}

/* 
    Time Complexity  : O(n)
    Space Complexity : O(n)

    The above approach works but it is not the correct interview method using recursions.

    Also the 'substring()' create new string repeatedly so it is O(n^2) but
    in DSA some in-build functions time complexity is neglected sometimes
*/


// 2nd Approach:

function isPalindrome(str) {

    if(str.length <= 1) {
        return true;
    }

    if(str[0] !== str[str.length - 1]) {
        return false;
    }

    return isPalindrome(str.substring(1, str.length - 1))
}


/*
    Time Complexity  : O(n)
    Space Complexity : O(n)
*/

/*  
    Explanation: 
    
    Recursive Palindrome Thinking:

    A string is palindrome if: first character == last character
    AND
    middle substring is also palindrome

    That is the recursive structure.

    Mathematically:

    Palindrome(s) = (s[0] == s[n-1])
    AND
    Palindrome(middle part)

    THIS is true recursive thinking.

    Recursive Breakdown Example: "ababa"

    Check: a == a

    Then solve smaller problem: "bab"

    Again: b == b

    Then solve: "a"
    
    Length: <= 1

    So: true

    Now: true propagates upward

    This is elegant recursion.
*/