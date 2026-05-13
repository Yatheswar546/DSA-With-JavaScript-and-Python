// Rotate an array k times to left and right in both cases. Don't create any new array.

function reverse(arr, start, end) {

    while(start < end) {
        let temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        start++;
        end--;
    }

}

// function leftRotate(arr, k) {
    
//     let n = arr.length;
//     k = k%n;

//     reverse(arr, 0, k-1);
//     reverse(arr, k, n-1);
//     reverse(arr, 0, n-1);

//     return arr;
// }

function rightRotate(arr, k) {

    let n = arr.length;
    k = k%n;

    reverse(arr, 0, n-k-1);
    reverse(arr, n-k, n-1);
    reverse(arr, 0, n-1);

    // 2nd approach
    /*
    reverse(arr, 0, n-1);
    reverse(arr, 0, k-1);
    reverse(arr, k, n-1);
    */

    return arr;
}

/* 
    For both cases:
    Time Complexity - O(n)
    Space Complexity - O(1)

*/