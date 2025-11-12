from typing import List


# https://leetcode.com/problems/contains-duplicate/?envType=problem-list-v2&envId=array
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        buff = {}

        for i in nums:
            if i not in buff:
                buff[i] = 1
            else:
                return True
        return False


sol = Solution()

ans = sol.containsDuplicate([1, 2, 3, 1])
print(ans)
