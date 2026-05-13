# Problem Description
# Write a program to calculate the simple interest based on the given principal amount, rate of interest, and time period.

# The formula to calculate simple interest is as follows:

# Simple Interest = (Principal × Rate × Time) / 100

# ​

# Input format
# The input consists of three space-separated integers on a single line:

# P (Principal amount)

# R (Rate of interest)

# T (Time period in years)

# Output format
# The program should output a single floating-point number representing the calculated simple interest, rounded to two decimal places.

# Sample Input 1
# 1000 5 2

# Sample Output 1
# 100.00

# Explanation
# For a principal amount of 1000, a rate of interest of 5%, and a time period of 2 years, the simple interest is calculated as follows:

# Simple Interest = (1000×5×2)/100 = 100.00

# Constraints
# 1 ≤ P ≤ 10^5

# 1 ≤ R,T ≤ 100

# Code 
principal = int(input("Enter Principal Amount: "))
rate_of_interest = int(input("Enter Rate of Interest: "))
time = int(input("Enter Time Period: "))

Simple_Interest = (principal * rate_of_interest * time) / 100

print(round(Simple_Interest, 2));


# Time Complexity - O(1)
# Space Complexity - O(1)