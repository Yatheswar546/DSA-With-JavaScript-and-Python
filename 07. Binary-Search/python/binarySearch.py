# Problem Description 

# Implement Binary Search

def binarySearch(arr, target):

    left = 0
    right = len(arr)-1

    while(left <= right):

        mid = (left + right) // 2

        if(arr[mid] == target):
            return True
        elif(arr[mid] < target):
            right = mid - 1
        elif(arr[mid] > target):
            left = mid + 1
    
    return False

arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

print(binarySearch(arr, target));

# Time Complexity  : O(log n)
# Space Complexity : O(1)