# Problem Description

# Implement the function stringCompression() that:
# Accepts a string s as an argument
# Returns
# a compressed string for each group of consecutive repeated characters by replacing the group with the character followed by the number of occurrences.
# the original string if the compressed string is not shorter than the original string

# Note
# You can assume the string contains only uppercase and lowercase letters (a-z).

# Input Format
# A single line containing the string s.

# Output Format
# A single line representing the compressed string as specified. If compression does not reduce the size, return the original string.

# Sample Input 1
# aabccccc

# Sample Output 1
# a2b1c5

# Explanation 1
# First 'a' repeats two times, then 'b' repeats once, then 'c' repeats two times.

# Constraints
# 1 <= length(S) <= 100000

# Code

s = input("Enter String: ")
n = len(s)

res = ''
count = 1

for i in range(1, n):

    if(s[i] == s[i-1]):
        count+=1

    elif(s[i] != s[i-1]):
        res += s[i-1]
        res += str(count)
        count = 1

res += s[n-1]
res += str(count)

print(res)

# Time Complexity  : O(n)
# Space Complexity : O(n)