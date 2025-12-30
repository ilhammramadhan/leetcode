class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        if R < 3 or C < 3:
            return 0
        
        def isMagic(r, c):
            # 1. The center of any 3x3 magic square of 1-9 MUST be 5
            if grid[r+1][c+1] != 5:
                return False
            
            # 2. Check for distinct 1-9 using a Bitmask (extremely fast)
            mask = 0
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    val = grid[i][j]
                    if val < 1 or val > 9: return False
                    mask |= (1 << val)
            
            # 0b1111111110 (bits 1 through 9 set) is 1022
            if mask != 1022:
                return False
            
            # 3. Minimal Sum Checks 
            # (If center is 5 and numbers are 1-9, we only need a few checks)
            return (grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15 and  # Row 0
                    grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15 and  # Row 2
                    grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15 and  # Col 0
                    grid[r][c] + grid[r+2][c+2] == 10) # Diagonal (must be 10 because center is 5)

        count = 0
        for r in range(R - 2):
            for c in range(C - 2):
                if isMagic(r, c):
                    count += 1
        return count