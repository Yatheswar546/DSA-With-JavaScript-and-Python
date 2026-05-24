# Problem Description: Find the power of a number pow(base, exponent)

# Input  : base = 2, exponent = 3
# Output : 8

# 1st Approach:
def powerofN(base, exponent):

    if(exponent == 0):
        return 1
    
    return base * powerofN(base, exponent-1);

base = int(input("Enter base value: "))
exponent = int(input("Enter exponent value: "))

print(powerofN(base, exponent))