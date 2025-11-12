// difficulty: medium
// https://leetcode.com/problems/3sum/
// TODO: Fix - not passing all tests on leetcode.com
function threeSum(nums) {
    // Sort
    nums.sort(function (a, b) { return a - b; });
    var i = 0;

    var buff: Set<number[]> = new Set();
    var TARGET_SUM = 0;

    while (i < nums.length - 2) {
        var first = nums[i];

        var j = i + 1;
        var k = nums.length - 1;
        
	while (j < k) {
            var second = nums[j];
            var third = nums[k];
            var runningSum = first + second + third;
            // console.log({ first, second, third, runningSum })
            if (runningSum > TARGET_SUM) {
                k -= 1;
            }
            else if (runningSum < TARGET_SUM) {
                j += 1;
            }
            else {
                // console.log(first, second, third)
                buff.add([first, second, third]);
                j += 1;
                k -= 1;
            }
        }
        i += 1;
    }
    return Array.from(buff);
}
console.log(threeSum([-1, 0, 1, 2, -1, -4]));
