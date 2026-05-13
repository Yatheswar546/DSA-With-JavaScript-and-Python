# Problem Description
# Given an array of n strings. Sort the array in lexicographical order.

# Input format
# First line contains integer n.

# Next line contains n space separated strings.

# Output format
# Print the sorted array.

# Sample Input 1
# 4

# abc abd ab a

# Sample Output 1
# a ab abc abd

# Explanation
# The given array is sorted in lexicographical order.

# Constraints
# 1 <= n <= 10000

# Strings contain only lowercase english alphabet.

# Each string will have length no more than 15.

n = int(input("Enter Array Size: "))
arr = list(map(str, input("Enter array elements: ").split()))

arr.sort()

print(arr);

# Time Complexity - O(n^2) || O(nlogn)