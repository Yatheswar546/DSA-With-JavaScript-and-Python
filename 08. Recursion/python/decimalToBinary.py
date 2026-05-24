'''
Problem Description: Convert the input number N from decimal to binary

Input  : 10 
Output : 1010

Input  : 12
Output : 1100

Input  : 16
Output : 10000

Input  : 25 
Output : 11001
'''

def binary(n):

    if(n==0): return ""
        
    return binary(n//2) + str(n%2)

n = int(input("Enter Decimal Number: "))
print("Binary Number: ", binary(n));

'''
    Time Complexity  : O(logn)
    Space Complexity : O(logn)

    Because for each recursive call, it reduced to half (1/2)
    let us say for n = 10, ==> 10 → 5 → 2 → 1 → 0
    
    So, n → n/2 → n/4 → n/8 → n/16 ........ → n/(2^k)

    So, Tc = O(logn) and call stack also fills in same way so Sp = O(logn)
'''