from typing import List

"""
    This is a very naive approach: 
    - Where we merge the 2 arrays and then perform a sort operation on the result
"""
class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
		x = m
		y = 0
		while x < len(nums1):
			nums1[x], nums2[y] = nums2[y], nums1[x]
			x += 1
			y -= 1
		nums1.sort()

		return nums1

solution = Solution()
res = solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

print(res)
assert res == [1,2,2,3,5,6]


