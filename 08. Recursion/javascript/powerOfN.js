// Problem Description: Find the power of a number pow(base, exponent)

// Input  : base = 2, exponent = 3
// Output : 8

// 1st Approach:
function powerOfN(base, exponent) {

    if(exponent == 0 ) {
        return 1;
    }

    return base * powerOfN(base, exponent-1);

}

let ans = powerOfN(2, 3)
console.log(ans);

/*
    Time Complexity  : O(n)
    Space Complexity : O(n)
*/


// 2nd Approach : Optimized Solution

function powerOfN(base, exponent) {

    if(exponent == 0 ) {
        return 1;
    }

    let half = powerOfN(base, Math.floor(exponent / 2));

    if(exponent % 2 == 0) {
        return half * half;
    }

    else {
        return base * half * half;
    }

}

/*
    Explanation: In mathematical expression, a^n can be calculated as:

    if n is even => a^n = (a^(n/2))^2

    if n is odd  => a^n = a * (a^((n-1)/2))^2

    based on this we can decrease exponent by half (1/2) on each recursive then

    n --> n/2 --> n/4 --> n/8 ....... n/(2^k)

    So, Time Complexity  = O(logn)
        Space Complexity = O(logn)
*/
