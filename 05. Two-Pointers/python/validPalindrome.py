# LeetCode - Problem 9

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

def validPalindrome(str):

    lowerCaseStr = str.lower()

    leftPtr = 0
    rightPtr = len(str)-1

    while(leftPtr < rightPtr):

        i = lowerCaseStr[leftPtr]
        j = lowerCaseStr[rightPtr]

        if(i.isalnum() and j.isalnum()):
            if( i != j ):
                return False
            leftPtr += 1
            rightPtr -= 1
        
        elif not(i.isalnum()):
            leftPtr += 1
        elif not(j.isalnum()):
            rightPtr -= 1

    return True;
    
str = input("Enter the sentence: ");
print(validPalindrome(str));

# Time Complexity  : O(n)
# Space Complexity : O(1)