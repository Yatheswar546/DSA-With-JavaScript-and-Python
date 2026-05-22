# Problem Description
# Given the array of integers nums of size n, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

# Input format
# First line contains n, the number of distinct integers.
# Second line contains n space separated integers

# Output format
# Print the maximum product.

# Sample Input 1
# 4
# 3 4 5 2

# Sample Output 1
# 12

# Explanation
# If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)(nums[2]-1) = (4-1)(5-1) = 3*4 = 12.

# Sample Input 2
# 4
# 1 5 4 5

# Sample Output 2
# 16

# Explanation
# Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

# Constraints
# 2 <= n <= 500
# 1 <= nums[i] <= 10^3

# Code

def maxProduct(nums):

    n = len(nums)
    max1 = 0
    max2 = 0
    count = 1

    for i in range(n):
        if(nums[i] == max1):
            count+=1
        
        elif(nums[i] > max1):
            max1 = nums[i]
            count = 1
    
    if(count >= 2):
        return (max1-1) * (max1-1)

    else:
        for i in range(n):
            if(nums[i] > max2 and nums[i] < max1):
                max2 = nums[i]

        return (max1-1) * (max2-1)
    
nums = list(map(int, input("Enter array numbers: ").split()))
print(maxProduct(nums))

# Time Complexity  : O(n)
# Space Complexity : O(1) 