class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # 1. Prefix sums for rows
        # row_sum[i][j] = sum(grid[i][0...j-1])
        row_sum = [[0] * (n + 1) for _ in range(m)]
        for r in range(m):
            for c in range(n):
                row_sum[r][c+1] = row_sum[r][c] + grid[r][c]
                
        # 2. Prefix sums for columns
        # col_sum[c][i] = sum(grid[0...i-1][c])
        col_sum = [[0] * (m + 1) for _ in range(n)]
        for c in range(n):
            for r in range(m):
                col_sum[c][r+1] = col_sum[c][r] + grid[r][c]

        def is_magic(r, c, k):
            # Calculate target sum using the first row of this kxk square
            target = row_sum[r][c + k] - row_sum[r][c]
            
            # Check all rows
            for i in range(r + 1, r + k):
                if row_sum[i][c + k] - row_sum[i][c] != target:
                    return False
            
            # Check all columns
            for j in range(c, c + k):
                if col_sum[j][r + k] - col_sum[j][r] != target:
                    return False
            
            # Check main diagonal
            diag1 = 0
            for i in range(k):
                diag1 += grid[r + i][c + i]
            if diag1 != target:
                return False
            
            # Check anti-diagonal
            diag2 = 0
            for i in range(k):
                diag2 += grid[r + i][c + k - 1 - i]
            return diag2 == target

        # 3. Search from largest k down to 2 (1 is always magic)
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
        return 1