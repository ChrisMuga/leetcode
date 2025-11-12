# difficulty: easy
# https://leetcode.com/problems/binary-search/


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        x = 0
        y = len(nums) - 1

        while x <= y:
            if nums[x] == target:
                return x
            elif nums[y] == target:
                return y
            x += 1
            y -= 1

        return -1


solution = Solution()
ans = solution.search([5], 5)
print(ans)
