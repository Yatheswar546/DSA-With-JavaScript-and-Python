# LeetCode Problem - 231

# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:
# Input: n = 1
# Output: true
# Explanation: 20 = 1

# Example 2:
# Input: n = 16
# Output: true
# Explanation: 24 = 16

# Example 3:
# Input: n = 3
# Output: false
 
# Constraints:
# -231 <= n <= 231 - 1

def isPowerofTwo(n):

    if( n.is_integer() and n==1 ):
        return True
    
    elif( not(n.is_integer()) or n<=0 ):
        return False
    
    else:
        return isPowerofTwo(n/2)
    
n = int(input("Enter n:"))
print(isPowerofTwo(n))

# Time Complexity  : O(logn)
# Space Complexity : O(logn)

# The recursion repeatedly does: n → n/2 → n/4 → n/8 ...
# So number of recursive calls becomes: log₂(n)

# Recursive call stack stores: log n function calls.