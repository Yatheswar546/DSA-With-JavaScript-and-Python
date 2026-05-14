# Leetcode Problem - 541

# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:

# Input: s = "abcd", k = 2
# Output: "bacd"
 
# Constraints:

# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 104

def reverseString(str, k):

    arr = list(str)
    
    i=0
    while(i < len(arr)):

        start = i
        end = min(i + k -1, len(arr)-1)

        while(start < end):
            arr[start], arr[end] = arr[end], arr[start]

            start += 1
            end -= 1

        i += 2*k

    return ''.join(arr);


str = input("Enter string: ")
k = int(input("Enter k: "))
print(reverseString(str, k))

# Time Complexity  : O(n)
# Space Complexity : O(n)