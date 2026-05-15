// Problem Description 

// Implement Binary Search

function binarySearch(arr, target) {

    let left = 0;
    let right = arr.length-1;

    while(left <= right) {

        let mid = Math.floor((left + right) / 2);

        if(arr[mid] ===  target) {
            return true
        }
        else if(arr[mid] > target) {
            right = mid - 1;
        }
        else if(arr[mid] < target) {
            left = mid + 1;
        }
    }
    return false;

}

binarySearch([1,2,3,4,5], 1);

/*
    Time Complexity  : O(log n)
    Space Complexity : O(1)
*/
 