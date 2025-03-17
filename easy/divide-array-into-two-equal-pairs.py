# difficutly: easy
# https://leetcode.com/problems/divide-array-into-equal-pairs/description 
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        pairs = {}
        keys = []

        for num in nums:
            if pairs.get(num) != None:
                pairs[num] += 1
            else:
                pairs[num] = 1
                keys.append(num)

        for key in keys:
            condition = pairs.get(key) % 2 == 0
            if condition:
                continue
            else:
                return False

        return True

# sample = [3,2,3,2,2,2]
sample = [1,2,3,4]
solution = Solution()
ans = solution.divideArray(sample)
print(ans)
