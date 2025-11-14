from typing import List

"""
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0

Strategy
----
While traversing the 2D matrix, if you find land: increment the number of islands found then...
Use DFS to mark your current position (land in this case), and other adjascent positions as water if they are not land 
but if you find land:
1. First mark it as water then
2. Then call the dfs method recursively on adjascent nodes/positions
"""


class Solution:
	def dfs(self, grid: List[List[str]], r: int, c: int):
		within_row_bounds = 0 <= r < len(grid)
		within_col_bounds = 0 <= c < len(grid[0])
		not_land = grid[r][c] != "1"

		out_of_bounds = not within_row_bounds or not within_col_bounds

		if out_of_bounds or not_land:
			return
		else:
			# Mark water
			grid[r][c] = "0"

			# Do dfs on adjascent nodes
			self.dfs(grid, r, c+1)
			self.dfs(grid, r, c-1)
			self.dfs(grid, r+1, c)
			self.dfs(grid, r-1, c)


	def numIslands(self, grid: List[List[str]]) -> int:
		rows, cols = len(grid), len(grid[0])
		count = 0

		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == "1":
					count += 1
					self.dfs(grid, r, c)
		return count


solution = Solution()
sample = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

res = solution.numIslands(sample)

print(res)
assert res == 1, "Expected only 1 island"
