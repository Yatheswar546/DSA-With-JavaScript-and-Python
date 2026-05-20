// Leetcode Problem: 242

// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// Example 1:
// Input: s = "anagram", t = "nagaram"
// Output: true

// Example 2:
// Input: s = "rat", t = "car"
// Output: false

// Constraints:
// 1 <= s.length, t.length <= 5 * 104
// s and t consist of lowercase English letters.

var isAnagram = function(s, t) {

    if(s.length != t.length) {
        return false;
    }

    let str1 = {}
    for(let char of s){
        if(str1[char]) {
            str1[char] +=1
        }
        else {
            str1[char] = 1
        }
    }

    let str2 = {}
    for(let char of t){
        if(str2[char]) {
            str2[char] +=1
        }
        else {
            str2[char] = 1
        }
    }

    for(let key in str1) {
        if(!(key in str2)) {
            return false
        }
        else {
            if(str1[key] !== str2[key]) {
                return false
            }
        }
    }

    return true

};

/*
    Time Complexity  : O(s)
    Space Complexity : O(s)
*/