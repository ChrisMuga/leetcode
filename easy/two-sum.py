# difficulty: easy
# https://leetcode.com/problems/two-sum/description/

from typing import List


class Solution:
    def twoSum(self, nums, target):
        pairs = {}

        # Load pairs
        for idx, num in enumerate(nums):
            diff = target - num
            match = pairs.get(num)
            if match != None:
                return [match, idx]
            else:
                pairs[diff] = idx


solution = Solution()
ans = solution.twoSum([2, 7, 11, 15], 9)
print(ans)
