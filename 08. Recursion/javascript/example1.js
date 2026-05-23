function printN(n) {

    if(n<=0) {
        return;
    }

    printN(n-1);
    console.log(n);
    printN(n-1);

}

printN(3)

/*
    Output:
    1
    2
    1
    3
    1
    2
    1
*/

/*
    Explanation:

    Stack:
        printN(0)
        printN(1)
        printN(2)

        printN(0) - Base condition TRUE.
        Immediately: return

    Stack pops:
        printN(1)
        printN(2)

    now execution resumes and prints 

    MOST IMPORTANT UNDERSTANDING
    Each function has:
        1. Left recursion
        2. Current work
        3. Right recursion

    This structure is VERY important later in:
        Trees
        DFS
        Backtracking
        
    Visual Recursion Tree

    For: printN(2)

    Tree Becomes:

                 3
            /        \
           2          2
         /   \       /   \
        1     1     1     1
       / \   / \   / \   / \
       0  0  0  0  0  0  0  0

    Now: printing happens in middle
    after: left recursion
    before: right recursion

    That is why order becomes: 1 2 1

*/

/*
    Time Complexity  : O(2^n)
    Space Complexity : O(n)

*/