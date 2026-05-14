# Problem Description
# Write a program that reverses a string.

# Input format
# First line will be a single string

# Output format
# 1<=size(S)<=200000

# Sample Input 1
# abc

# Sample Output 1
# cba

# Explanation
# cba is reverse of abc.

# Sample Input 2
# aaa

# Sample Output 2
# aaa

# Explanation
# aaa is reverse of aaa.

# Constraints
# Print the reverse of the string in a single line.

def reverseString(str):

    arr = list(str);

    leftPtr = 0;
    rightPtr = len(arr)-1;

    while(leftPtr < rightPtr):
        arr[leftPtr], arr[rightPtr] =  arr[rightPtr], arr[leftPtr]

        leftPtr += 1;
        rightPtr -= 1;

    return ''.join(arr);

str = input("Enter the string: ");
print(reverseString(str));


