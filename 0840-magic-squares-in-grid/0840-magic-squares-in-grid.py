class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        def isMagic(r, c):
            # 1. Quick check: Center must be 5
            if grid[r+1][c+1] != 5:
                return False
            
            # 2. Check for distinct numbers 1-9
            vals = []
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    vals.append(grid[i][j])
            if sorted(vals) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
            
            # 3. Check Rows and Columns sum (must be 15)
            # We don't need to check all if we trust the math, 
            # but for clarity:
            for i in range(3):
                # Rows
                if sum(grid[r+i][c:c+3]) != 15: return False
                # Columns
                if grid[r][c+i] + grid[r+1][c+i] + grid[r+2][c+i] != 15: return False
                
            # 4. Check Diagonals
            diag1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
            diag2 = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]
            
            return diag1 == 15 and diag2 == 15

        # Move the 3x3 window across the grid
        for r in range(rows - 2):
            for c in range(cols - 2):
                if isMagic(r, c):
                    count += 1
                    
        return count