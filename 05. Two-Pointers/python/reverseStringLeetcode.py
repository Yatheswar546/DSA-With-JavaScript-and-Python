# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 
# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.


def reverseString(str):

    leftPtr = 0
    rightPtr = len(str)-1 

    while(leftPtr < rightPtr):
        str[leftPtr], str[rightPtr] = str[rightPtr], str[leftPtr]

        leftPtr += 1
        rightPtr -= 1

    return str

str = input("Enter the string: ").split();
print(reverseString(str));

# Time Complexity  : O(n)
# Space Complexity : O(1)