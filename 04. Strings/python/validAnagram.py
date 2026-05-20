# Leetcode Problem: 242

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

def validAnagram(s, t):

    if(len(s) != len(t)):
        return "false"

    else:
        str1 = {}

        for i in s:
            if i in str1:
                str1[i] +=1
            else:
                str1[i] = 1
    
        str2 = {}

        for i in t:
            if i in str2:
                str2[i] +=1
            else:
                str2[i] = 1

        for i in str1:

            if(i not in str2):
                return "false"
            else:
                if(str1[i] != str2[i]):
                    return "false"
        
        return "true"
            
print(validAnagram("python","nothypp"))


# Time Complexity  : O(s)
# Space Complexity : O(s)