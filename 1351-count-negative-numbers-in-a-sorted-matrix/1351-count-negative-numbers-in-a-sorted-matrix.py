class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)    # Number of rows
        n = len(grid[0]) # Number of columns
        
        # Start at the bottom-left corner
        row = m - 1
        col = 0
        count = 0
        
        # Loop as long as we are inside the grid boundaries
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                # If current number is negative, 
                # all numbers to its right in this row are also negative.
                # n - col gives us the number of remaining elements in the row.
                count += (n - col)
                
                # Since we handled this row's negative contribution (from this point),
                # we move up to check the previous row.
                row -= 1
            else:
                # If current number is positive/zero,
                # we need to move right to find smaller numbers.
                col += 1
                
        return count