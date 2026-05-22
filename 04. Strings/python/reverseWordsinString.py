# Problem Description:

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words.

# The returned string should only have a single space separating the words.

# Do not include any extra spaces.

# Input format
# String s.

# Output format
# The function should return a string of the words in reverse order concatenated by a single space.

# Sample Input 1
# hello world

# Sample Output 1
# world hello

# Explanation
# The given words after being reversed gives:world hello

# Your reversed string should not contain leading or trailing spaces.

# Constraints
# 1 <= s.length <= 10^5

# s contains English letters (upper-case and lower-case), digits, and spaces ' '.

# There is at least one word in s.

# Code

s = input("Enter String: ")
n = len(s)

word = ""
finalString = ""

i=n-1
while(i>=0):    
    
    if(s[i]== ' '):
        i-=1
        continue;

    else:
        while(s[i]!=' ' and i>=0):    
            word += s[i]
            i-=1

        for j in range(len(word)-1, -1, -1):
            finalString += word[j]
        
        while(i>=0 and s[i]==' '):
            i-=1

        if(i>=0):
            finalString += ' '

        word = ''

print(finalString);

# Time Complexity  : O(n)
# Space Complexity : O(n)