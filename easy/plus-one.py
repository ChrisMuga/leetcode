# https://leetcode.com/problems/plus-one/

"""
Strategy:

Loop from right to left,
	- If you run into a value that is < 9: Increment it and return early
	- If you run into a 9, convert it into 0
At the end of the loop if the conditions above are not met, then it means the values were all 9's
Prepend a 1 at the beginning and return the array
"""
from typing import List

class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		left = len(digits) - 1

		while left >= 0:
			if digits[left] < 9:
				digits[left] += 1
				return digits
			digits[left] = 0 
			left -= 1

		return [1] + digits

solution = Solution()
sample = [1, 4, 9]
res = solution.plusOne(sample)

print(res)
assert res == [1, 5, 0], "[1, 5, 0] Expected"
	
