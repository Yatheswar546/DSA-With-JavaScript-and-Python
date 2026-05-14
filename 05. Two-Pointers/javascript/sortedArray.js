// Problem Description:

// Check if an array is sorted or not.

// Input:
// First line contains an integer representing the size of array.

// Second line contains 'n' numbers 

// Output: 
// Yes (or) No

function sortedArray(arr) {

    let pointer1 = 0;
    let pointer2 = 1;

    while(pointer2 < arr.length) {

        if(arr[pointer1] > arr[[pointer2]]) {
            return false;
        }

        pointer1++;
        pointer2++;

    }

    return true;

}

/*
    Time Complexity  : O(n)
    Space Complexity : O(1)
*/