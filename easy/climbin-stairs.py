"""
    difficulty: easy
    https://leetcode.com/problems/climbing-stairs/description/
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1

        return self.climbStairs(n -1) + self.climbStairs(n - 2)


solution = Solution()
print(solution.climbStairs(3))
