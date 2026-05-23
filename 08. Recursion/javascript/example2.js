function fun(n) {

    if(n==0) {
        return;
    }

    console.log("Start: ", n);
    fun(n-1);
    console.log("End: ", n);
}

fun(3);

/*
    Start: 3
    Start: 2
    Start: 1
    End: 1
    End: 2
    End: 3
*/

/*
    Explanation:

        Before Base Condition

        Stack: 
            fun(1)
            fun(2)
            fun(3)

        prints: 
            Start: 3
            Start: 2
            Start: 1      
            
        After Base Condition: fun(0)

        Stack Pops: 
            fun(1)
            fun(2)
            fun(3)

        now prints:
            End: 1
            End: 2
            End: 3

    This example teaches:
        Before recursion: work happens during downward phase
        After recursion: work happens during stack unwinding phase

    Golden Recursion Mental Model
        Every recursive function has:
            1. Before recursive call
            2. Recursive call
            3. After recursive call

    Understanding: BEFORE vs AFTER recursion

    This exact pattern is used in:
        Tree Traversals
        DFS
        Backtracking
        Dynamic Programming
        Graph Algorithms

    Especially: preorder / inorder / postorder

    all come from: where work is done relative to recursion
*/

/*
    Time Complexity  : O(n)
    Space Complexity : O(n)
*/