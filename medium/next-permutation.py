from typing import List

class Solution:
	def nextPermutation(self, nums: List[int]) -> None:
		i = len(nums) - 2

		# Find where the increasing sequence is broken, starting from the right
		while i >= 0: 
			if nums[i] < nums[i + 1]:
				break
			i -= 1

		if i >= 0: # This means we found a pivot (i.e: where the increasing sequence is broken starting from the right)
			# If we've found a pivot, then find the smallest number that is greater than the number at the pivot, in the whole array
			x = len(nums) - 1

			while nums[x] <= nums[i] and x >=0:
				x -= 1

			# So then the smallest number that is greater than the number at the pivot is at x
			# Since we're navigating from right to left, when we reach the break point, the entries right to it are already sorted in descending order
			nums[x], nums[i] = nums[i], nums[x]

		self.reverseFrom(nums, i + 1)

		print(nums)
	
	def reverseFrom(self, nums: List[int], idx: int) -> None:
		idy = len(nums) - 1

		while idx <= idy:
			nums[idx], nums[idy] = nums[idy], nums[idx]
			idx += 1
			idy -= 1

solution = Solution()
sample = [5,1,1]

ans = solution.nextPermutation(sample)

