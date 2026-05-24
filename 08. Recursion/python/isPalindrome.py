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
# def isPalindrome(str):

#     if(len(str)<=1):
#         return str;

#     return isPalindrome(str[1:]) + str[0];

# str = input("Enter the string: ");
# reversedStr = isPalindrome(str);

# if(str == reversedStr):
#     print(True);
# else:
#     print(False);

'''
    Time Complexity  : O(n)
    Space Complexity : O(n)

    The above approach works but it is not the correct interview method using recursions.
'''

# 2nd Approach
def isPalindrome(str):

    if(len(str)<=1):
        return True
    
    elif(str[0] != str[-1]):
        return False 

    else:
        return isPalindrome(str[1: len(str)-1])

str = input("Enter the string: ");
print(isPalindrome(str));

'''
    Time Complexity  : O(n)
    Space Complexity : O(n)
'''

'''
    Explanation: 
    
    Recursive Palindrome Thinking:

    A string is palindrome if: first character == last character
    AND
    middle substring is also palindrome

    That is the recursive structure.

    Mathematically:

    Palindrome(s) = (s[0] == s[n-1])
    AND
    Palindrome(middle part)

    THIS is true recursive thinking.

    Recursive Breakdown Example: "ababa"

    Check: a == a

    Then solve smaller problem: "bab"

    Again: b == b

    Then solve: "a"
    
    Length: <= 1

    So: true

    Now: true propagates upward

    This is elegant recursion.
'''