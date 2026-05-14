// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Note that you must do this in-place without making a copy of the array.

 

// Example 1:

// Input: nums = [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Example 2:

// Input: nums = [0]
// Output: [0]
 

// Constraints:

// 1 <= nums.length <= 104
// -231 <= nums[i] <= 231 - 1

var moveZeroes = function(nums) {
    
    firstPtr = 0;
    secondPtr = 1;
    
    while(secondPtr < nums.length) {
        if(nums[firstPtr] == 0 && nums[secondPtr] != 0) {
            let temp = nums[firstPtr];
            nums[firstPtr] = nums[secondPtr];
            nums[secondPtr] = temp;
            
            firstPtr++;
            secondPtr++;
        }
        else if(nums[firstPtr]==0 && nums[secondPtr]==0) {
            secondPtr++;    
        }
    }
    
    return nums;
    
};

/*
    Time Complexity  : O(n)
    Space Complexity : O(1)
*/