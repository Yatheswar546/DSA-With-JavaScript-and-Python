# Problem Description: Find the power of a number pow(base, exponent)

# Input  : base = 2, exponent = 3
# Output : 8

# 1st Approach:
# def powerofN(base, exponent):

#     if(exponent == 0):
#         return 1
    
#     return base * powerofN(base, exponent-1);

# base = int(input("Enter base value: "))
# exponent = int(input("Enter exponent value: "))

# print(powerofN(base, exponent))

# Time Complexity  : O(n)
# Space Complexity : O(n)


# 2nd Approach : Optimized Solution

def powerofN(base, exponent):

    if(exponent == 0): 
        return 1

    half = powerofN(base, (exponent//2))

    if(exponent % 2 == 0):
        return half * half 
    
    elif(exponent % 2 != 0):
        return base * half * half
    
base = int(input("Enter base value: "))
exponent = int(input("Enter exponent value: "))

print(powerofN(base, exponent))

'''
    Explanation: In mathematical expression, a^n can be calculated as:

    if n is even => a^n = (a^(n/2))^2

    if n is odd  => a^n = a * (a^((n-1)/2))^2

    based on this we can decrease exponent by half (1/2) on each recursive then

    n --> n/2 --> n/4 --> n/8 ....... n/(2^k)

    So, Time Complexity  = O(logn)
        Space Complexity = O(logn)
'''