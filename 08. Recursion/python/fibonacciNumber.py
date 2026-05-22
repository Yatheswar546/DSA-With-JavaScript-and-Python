# Leetcode Problem : 509

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 
# Constraints:
# 0 <= n <= 30

# Recursive Approach

def fibonacciNumber(n):

    if(n <= 1):
        return n;

    else:
        return fibonacciNumber(n-1) + fibonacciNumber(n-2);

# Time Complexity  : O(2^n)
# Space Complexity : O(n)


# Iterative Approach

def fibonacciNumber(n):

    a=0; b=1; c=0;

    if(n <= 1):
        return n 
    
    else:
        for i in range(2,n+1):
            c = a+b
            a = b
            b = c
    return c;

# Time Complexity  : O(n)
# Space Complexity : O(1)

n = int(input("Enter n: "))
print(fibonacciNumber(n))
