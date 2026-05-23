function fun(n) {
    if(n==1) {
        return 1;
    }
    return n + fun(n-1);
}
console.log(fun(4));

/*
    Input: n = 4
    Output: 10

    Input: n = 5
    Output: 15

*/

/*
    Explanation:

        Call Stack:
            fun(4)
            fun(3)
            fun(2)
            fun(1)

        After Base Condition n==1:
            4 + fun(3)  [6]            ==> 10
                 3 + fun(2) [3]        ==> 6
                        2 + fun(1) [1] ==> 3
                                1

        Addition happens in upward unwinding
    
*/

/*
    Time Complexity  : O(n)
    Space Complexity : O(n)
*/