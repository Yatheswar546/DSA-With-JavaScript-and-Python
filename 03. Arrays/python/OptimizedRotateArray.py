# Problem Description
# You are given a array of numbers. Your task is to rotate the given array left(anti-clockwise) and right(clockwise) by n units from the starting index. 
# You are required to return the rotated array.

# Input format
# First line contains an integer n, the size of the array and k the number of rotations. 
# Second line contains n integers, the elements of the array.

# Output format
# Return the rotated string.

# Sample Input 1
# 5 1
# 1 2 3 4 5

# Sample Output 1
# 2 3 4 5 1

# Explanation
# In the left rotation, the subarray of length 1 from the beginning is [1], this subarray is removed from the beginning and attached to the end of the array(i.e. anti-clockwise).

# Sample Input 2
# 5 2
# 1 2 3 4 5

# Sample Output 2
# 3 4 5 1 2

# Constraints
# 1 <= n <= 10^5 1 <= arr[i] <= 10^5

n, k = map(int, input("Enter n and k: ").split())
arr = list(map(int, input("Enter array elements: ").split()))

def reverse(arr, start, end):

    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp 

        start += 1
        end -= 1
    
    return arr


def leftRotate(arr, k):

    k = k % n

    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)

    return arr 


def rightRotate(arr, k):

    k = k % n

    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)

    return arr 

print("Left Rotation: ", leftRotate(arr.copy(), k))
print("Right Rotation: ", rightRotate(arr.copy(), k))

# For both cases:
#     Time Complexity - O(n)
#     Space Complexity - O(1)