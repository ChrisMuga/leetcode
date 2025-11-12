# difficulty: easy
# https://leetcode.com/problems/remove-element/description/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for num in nums:
            if num != val:
                nums[idx] = num
                idx += 1

        return idx


# Run
solution = Solution()
ans = solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(ans)
