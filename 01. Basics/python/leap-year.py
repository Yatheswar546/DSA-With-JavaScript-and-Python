# Problem Description
# For an input year N, find whether the year is a leap or not.

# Input format
# First line contains an integer - N.

# Output format
# Print "true" if it is a leap year otherwise "false".

# Sample Input 1
# 1600

# Sample Output 1
# true

# Explanation
# Year 1600 is a leap year

# Sample Input 2
# 1800

# Sample Output 2
# false

# Explanation
# Year 1800 is not a leap year

# Constraints
# 1 <= N <= 9999


year = int(input("Enter year: "))

if((year % 4==0 and year % 100 !=0) or year % 400 == 0):
    print("Leap Year");
else:
    print("Non-leap Year");