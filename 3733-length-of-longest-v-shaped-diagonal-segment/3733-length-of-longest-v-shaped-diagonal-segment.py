from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        # If no '1' exists, no segment can start.
        if not any(1 in row for row in grid):
            return 0
        max_len = 1

        def is_valid_next(val: int, prev_len: int) -> bool:
            if prev_len == 0: return False # Cannot continue a segment of length 0
            # Sequence: 1, 2, 0, 2, 0...
            if prev_len % 2 == 1: # After odd length (1, 3, ...), next should be 2
                return val == 2
            else: # After even length (2, 4, ...), next should be 0
                return val == 0

        # dp_s tables for Straight segments
        dp_s1 = [[0] * m for _ in range(n)] # tl_br
        dp_s2 = [[0] * m for _ in range(n)] # tr_bl
        dp_s3 = [[0] * m for _ in range(n)] # bl_tr
        dp_s4 = [[0] * m for _ in range(n)] # br_tl

        # dp_v tables for V-shaped segments
        dp_v1 = [[0] * m for _ in range(n)] # 2nd arm is tl_br (turn from bl_tr)
        dp_v2 = [[0] * m for _ in range(n)] # 2nd arm is tr_bl (turn from tl_br)
        dp_v3 = [[0] * m for _ in range(n)] # 2nd arm is bl_tr (turn from br_tl)
        dp_v4 = [[0] * m for _ in range(n)] # 2nd arm is br_tl (turn from tr_bl)

        ## ------------------------------------------------------------------
        ## FIRST, CALCULATE ALL STRAIGHT SEGMENTS (dp_s)
        ## ------------------------------------------------------------------
        
        # Pass 1: Top-down for dp_s1, dp_s2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: dp_s1[i][j] = 1
                elif i > 0 and j > 0 and is_valid_next(grid[i][j], dp_s1[i-1][j-1]):
                    dp_s1[i][j] = dp_s1[i-1][j-1] + 1
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 1: dp_s2[i][j] = 1
                elif i > 0 and j < m - 1 and is_valid_next(grid[i][j], dp_s2[i-1][j+1]):
                    dp_s2[i][j] = dp_s2[i-1][j+1] + 1
        
        # Pass 2: Bottom-up for dp_s3, dp_s4
        for i in range(n - 1, -1, -1):
            for j in range(m):
                if grid[i][j] == 1: dp_s3[i][j] = 1
                elif i < n - 1 and j > 0 and is_valid_next(grid[i][j], dp_s3[i+1][j-1]):
                    dp_s3[i][j] = dp_s3[i+1][j-1] + 1
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 1: dp_s4[i][j] = 1
                elif i < n - 1 and j < m - 1 and is_valid_next(grid[i][j], dp_s4[i+1][j+1]):
                    dp_s4[i][j] = dp_s4[i+1][j+1] + 1

        ## ------------------------------------------------------------------
        ## SECOND, CALCULATE ALL V-SHAPED SEGMENTS (dp_v) USING COMPLETED dp_s
        ## ------------------------------------------------------------------

        # Pass 3: Top-down for dp_v1, dp_v2
        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    cand_len = 0
                    first_arm = dp_s3[i-1][j-1]
                    if is_valid_next(grid[i][j], first_arm): cand_len = max(cand_len, first_arm + 1)
                    prev_v = dp_v1[i-1][j-1]
                    if is_valid_next(grid[i][j], prev_v): cand_len = max(cand_len, prev_v + 1)
                    dp_v1[i][j] = cand_len
            for j in range(m - 1, -1, -1):
                if i > 0 and j < m - 1:
                    cand_len = 0
                    first_arm = dp_s1[i-1][j+1]
                    if is_valid_next(grid[i][j], first_arm): cand_len = max(cand_len, first_arm + 1)
                    prev_v = dp_v2[i-1][j+1]
                    if is_valid_next(grid[i][j], prev_v): cand_len = max(cand_len, prev_v + 1)
                    dp_v2[i][j] = cand_len

        # Pass 4: Bottom-up for dp_v3, dp_v4
        for i in range(n - 1, -1, -1):
            for j in range(m):
                if i < n - 1 and j > 0:
                    cand_len = 0
                    first_arm = dp_s4[i+1][j-1]
                    if is_valid_next(grid[i][j], first_arm): cand_len = max(cand_len, first_arm + 1)
                    prev_v = dp_v3[i+1][j-1]
                    if is_valid_next(grid[i][j], prev_v): cand_len = max(cand_len, prev_v + 1)
                    dp_v3[i][j] = cand_len
            for j in range(m - 1, -1, -1):
                if i < n - 1 and j < m - 1:
                    cand_len = 0
                    first_arm = dp_s2[i+1][j+1]
                    if is_valid_next(grid[i][j], first_arm): cand_len = max(cand_len, first_arm + 1)
                    prev_v = dp_v4[i+1][j+1]
                    if is_valid_next(grid[i][j], prev_v): cand_len = max(cand_len, prev_v + 1)
                    dp_v4[i][j] = cand_len
        
        # Final pass to find the maximum length from all tables
        for i in range(n):
            for j in range(m):
                max_len = max(max_len, dp_s1[i][j], dp_s2[i][j], dp_s3[i][j], dp_s4[i][j],
                                     dp_v1[i][j], dp_v2[i][j], dp_v3[i][j], dp_v4[i][j])
                
        return max_len