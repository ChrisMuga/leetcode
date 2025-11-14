from typing import List

"""
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])

        return 0


solution = Solution()
sample = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

res = solution.numIslands(sample)

assert res == 1, "Expected only 1 island"
print(res)
        
