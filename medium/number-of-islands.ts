// https://leetcode.com/problems/number-of-islands/
function numIslands(grid: string[][]): number {
    var count = 0;
    // Find the number of rows and columns
    const rows = grid.length;
    const cols = grid[0].length;

    // Loop across all the entries of the matrix/grid
    for(var r = 0; r < rows; r+=1) {
        for(var c = 0; c < cols; c+=1) {
            // If you find land;
            //  - Increase the number of islands, then perform a DFS on that specific position
            //  - The DFS function in this case, takes the current position if it is land and marks it as water
            if(grid[r][c] == "1"){
                count += 1;
                dfs(grid, r, c)
            }
        }
    }

    return count
};

function dfs(grid: string[][], r:number, c: number) {
    // Here we check if the current position is within bounds or is land
    // - If it is not then exit out the function
    // - If it is then mark the position as water i.e "0"
    // - Then call DFS on the adjascent positions

    // Redundant but can be optimized
    const rows = grid.length;
    const cols = grid[0].length;

    const isLandWithinBounds = (r >= 0 && r < rows) && (c >= 0 && c < cols) && grid[r][c] == "1";

    if(isLandWithinBounds){
        // Mark the current position as water, i.e "0"
        grid[r][c] = "0";

        // Run DFS on adjascent nodes
        dfs(grid, r, c+1)
        dfs(grid, r, c-1);
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c)
    }else{
        return;
    }

}
