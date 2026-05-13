# Problem Description
# Given an array of integers, write a program to find the sum of the minimum and maximum values of the array.

# Input format
# First line contains an integer N, the size of the array

# Second line contains the integers present in the array

# Output format
# Return expected integer

# Sample Input 1
# 5

# 10 15 4 5 19

# Sample Output 1
# 23

# Explanation
# The minimum and maximum values of the array are 4 and 19 respectively, totaling 23

# Sample Input 2
# 3

# 10 10 10

# Sample Output 2
# 20

# Explanation
# The minimum and maximum values of the array are the same, i.e, 10, totaling 20

# Constraints
# 1 <= N <= 10^5

# 1 <= arr[i] <= 10^9

n = int(input("Enter the size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))

max = arr[0]
min = arr[0]

for i in range(n):
    if (arr[i] > max):
        max = arr[i]
    if (arr[i] < min):
        min = arr[i]

sum = max + min

print("Final Sum: ", sum)


# Time Complexity - O(n)
# Space Complexity - O(1)