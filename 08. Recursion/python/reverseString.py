def reverseStr(s):

    if(len(s) <= 1):
        return s    
        
    return reverseStr(s[1:]) + s[0]
    
str = input("Enter String: ")
print(reverseStr(str));

'''
    Time Complexity  : O(n^2)
    Space Complexity : O(n)

    O(n^2) is because "substring()" creates new string every call
    Each substring copy costs: O(n) and recursion happens n times. So Tc = O(n^2)
'''