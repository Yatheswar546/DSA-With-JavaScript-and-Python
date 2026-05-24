'''
Problem Description: Check if the given string is palindrome or not

Input  : ababa
Output : true

Input  : ababc
Output : false

Input  : abcba
Output : true
'''

# 1st Approach
def isPalindrome(str):

    if(len(str)<=1):
        return str;

    return isPalindrome(str[1:]) + str[0];

str = input("Enter the string: ");
reversedStr = isPalindrome(str);

if(str == reversedStr):
    print(True);
else:
    print(False);

'''
    Time Complexity  : O(n)
    Space Complexity : O(n)

    The above approach works but it is not the correct interview method using recursions.
'''

