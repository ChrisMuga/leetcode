// difficulty: medium
// https://leetcode.com/problems/3sum/

function threeSum(nums: number[]): number[][] {
	// Sort
	nums.sort((a, b) => a - b);

	let i = 0;

	const buff: number[][] = [];


	const TARGET_SUM = 0;

	while (i < nums.length - 2) {
		let first = nums[i];

		let j = i + 1;
		let k = nums.length - 1;

		while (j < k) {
			const second = nums[j];
			const third = nums[k];

			let runningSum = first + second + third;

			console.log({ first, second, third, runningSum })

			if (runningSum > TARGET_SUM) {
				k -= 1;
			} else if (runningSum < TARGET_SUM) {
				j += 1;
			} else {
				console.log(first, second, third)
				buff.push([first, second, third]);
				j += 1;
				k -= 1;
			}
		}

		i += 1;
	}

	return buff;
}

console.log(threeSum([-1, 0, 1, 2, -1, -4]))
