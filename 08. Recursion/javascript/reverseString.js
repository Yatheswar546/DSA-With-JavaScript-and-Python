var reverseStr = function(s) {

    if(s.length <= 1) {
        return s;
    }

    return reverseStr(s.substring(1)) + s[0];

}

/*
    Time Complexity  : O(n^2)
    Space Complexity : O(n)

    O(n^2) is because "substring()" creates new string every call
    Each substring copy costs: O(n) and recursion happens n times. So Tc = O(n^2)

*/
