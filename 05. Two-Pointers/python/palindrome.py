# Problem Description
# Given a string comprising only lowercase alphabets, determine whether it qualifies as a palindrome.

# A string is considered a palindrome if it reads the same forwards and backwards.

# Note:

# For the purpose of this problem, we define empty string as valid palindrome.

# Input format
# The only line contains a string.

# Output format
# True or False.

# Sample Input 1
# madam

# Sample Output 1
# true

# Explanation
# "madam" spelt backwards is "madam", therefore, it is a palindrome.

# Sample Input 2
# crio

# Sample Output 2
# false

# Explanation
# "crio" spelt backwards is "oirc", therefore, it is not a palindrome.

# Constraints
# 1 <= s.length <= 2 * 10^5

# Code 

def checkPalindrome(str):

    leftPtr = 0;
    rightPtr = len(str)-1;
    
    while(leftPtr < rightPtr):
        
        if(str[leftPtr] != str[rightPtr]):
            return False
        
        leftPtr += 1;
        rightPtr -= 1;

    return True;

str = input("Enter String: ");
print(checkPalindrome(str));

# Time Complexity  : O(n)
# Space Complexity : O(1)