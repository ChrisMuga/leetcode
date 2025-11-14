// https://leetcode.com/problems/next-permutation/
/**
 Do not return anything, modify nums in-place instead.
 */
function nextPermutation(nums: number[]): void {
    // Initialize the pivot/breakpoint
    var pivot = nums.length - 2;

    // Find the current pivot/breakpoint
    // i.e where nums[pivot + 1] > nums[pivot] 
    while(nums[pivot] >= nums[pivot+1]){
        pivot -= 1;
    }
    
    // Now that we've found our pivot;
    //  - Find the index of next number in the list that is > than the number at the pivot
    
    if(pivot >= 0){
        var i = nums.length - 1
        while(nums[pivot] >= nums[i]){
            i -= 1;
        }
    

        // Once we find the index of the next number that is > than the number at the pivot
        // - We swap them
        const x = nums[pivot]
        const y = nums[i]

        nums[pivot] = y
        nums[i] = x
    }

    // After swapping:
    // - Reverse the array from the next position after the pivot

    reverseNums(nums, pivot + 1)  
};

const reverseNums = (nums: number[], idx: number) => {
    var right = nums.length - 1

    while(idx <= right) {
        const x = nums[idx]
        const y = nums[right]

        nums[idx] = y
        nums[right] = x

        right -= 1;
        idx += 1
    }
}
