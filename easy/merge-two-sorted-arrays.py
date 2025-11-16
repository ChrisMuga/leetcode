from typing import List

class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		# Find the index of the last item in nums1, which will be our result/output
		last = m + n - 1

		# We're comparing the values of the last items, i.e from LEFT to RIGHT in both the arrays 
		# to identify which one should be the absolute last
		# so we start from the tail end of both arrays trying to fill the values at the end of nums1, with the larger values
		# - we're traversing both the arrays in reverse order

		while m > 0 and n > 0:
			x, y = nums1[m-1], nums2[n-1]

			if x > y:
				nums1[last] = x
				m -= 1
			else:
				nums1[last] = y
				n -= 1

			last -= 1

		# If there are any left-over items in nums2,
		# Since the arrays are both sorted in ascending order, we append the last items at the tail end of nums1

		while n > 0:
			nums1[last] = nums2[n - 1]
			n -= 1
			last -= 1

		return nums1
				
				

solution = Solution()

input_a, size_a = [4, 0, 0, 0, 0, 0], 1
input_b, size_b = [1, 2, 3, 5, 6], 5

res = solution.merge(input_a, size_a, input_b, size_b)

print("-->", res)

expected = [1, 2, 3, 4, 5, 6]

assert res == expected, f"{expected} is the expected output of .merge(), not {res}"
