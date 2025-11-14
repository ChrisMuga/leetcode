class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int):
            # Check if the current position is within bounds
            within_row = 0 <= r < rows
            within_col = 0 <= c < cols

            if not within_row or not within_col:
                return

            # Then check if the current position is land
            is_land = grid[r][c] == "1"

            # If the current position is land and within bounds:
            #   - Mark it as water/visited
            if is_land:
                grid[r][c] = "0"

                # After marking the position as water:
                # Recursively find adjascent positions and mark as water if conditions apply

                dfs(r, c + 1)
                dfs(r, c - 1)
                dfs(r + 1, c)
                dfs(r - 1, c)
            else:
                return



        for r in range(rows):
            for c in range(cols):
                # Check if we find land:
                if grid[r][c] == "1":
                    # First we increase the number of islands
                    number_of_islands += 1
                    # In which case we want to recursively mark adjascent nodes as water if they are indeed not "1"
                    dfs(r, c)

        return number_of_islands
