"""
    difficulty: easy
    https://leetcode.com/problems/climbing-stairs/description/
"""

class Solution:
    # # Using recursion - recursive backtracking
    # # O(2 ^ N)
    # def climbStairs(self, n: int) -> int:
    #     if n == 0:
    #         return 1
    #     if n == 1:
    #         return 1
    #
    #     return self.climbStairs(n -1) + self.climbStairs(n - 2)

    # O(N) - Backtracking
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        
        # initialize with (i-2) and (i-1)
        buff = [1, 1]

        for i in range(2, n + 1):
            buff.append(buff[i-1] + buff[i-2])

        return buff[n]



solution = Solution()
print(solution.climbStairs(3))
