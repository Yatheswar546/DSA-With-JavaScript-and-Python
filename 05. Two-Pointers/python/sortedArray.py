# Problem Description:

# Check if an array is sorted or not.

# Input:
# First line contains an integer representing the size of array.

# Second line contains 'n' numbers 

# Output: 
# Yes (or) No

def sortedArray(arr):

    firstPtr = 0
    secondPtr = 1

    while(secondPtr < len(arr)):
        if(arr[firstPtr] > arr[secondPtr]):
            return False
        
        firstPtr += 1
        secondPtr += 1
    
    return True

arr = list(map(int, input("Enter array: ").split()));
print(sortedArray(arr));

# Time Complexity  : O(n)
# Space Complexity : O(1)