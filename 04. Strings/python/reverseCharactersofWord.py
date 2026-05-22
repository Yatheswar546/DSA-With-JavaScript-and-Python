# Problem Description
# Write a program to reverse the words present in a sentence.

# Input format
# First line contains an string consisting of words separated by spaces.

# Output format
# Return the string with it's words reversed.

# Sample Input 1
# abc def ghi

# Sample Output 1
# cba fed ihg

# Explanation
# abc reversed is cba, def reversed is fed, ghi reversed is igh.

# Constraints
# 1 <= str.length <= 10^5

s = input("Enter String: ")
n = len(s)

finalString = ''
word = ''

for i in range(0, n):

    if (s[i]!=' '):
        word += s[i]

    else:
        for j in range(len(word)-1, -1, -1):  
            finalString += word[j]
        word = ''
        finalString += ' '

for i in range(len(word)-1, -1, -1):
    finalString += word[i]

print(finalString)

# Time Complexity  : O(n)
# Space Complexity : O(n)