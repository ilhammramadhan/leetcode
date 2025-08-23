import math
from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = float('inf')

        # Helper function to find the minimum bounding box area for all 1s in a subgrid
        def get_min_area(r1, c1, r2, c2):
            min_r, max_r = float('inf'), float('-inf')
            min_c, max_c = float('inf'), float('-inf')
            found_one = False
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if grid[r][c] == 1:
                        found_one = True
                        min_r = min(min_r, r)
                        max_r = max(max_r, r)
                        min_c = min(min_c, c)
                        max_c = max(max_c, c)
            
            # If a subgrid has no 1s, this partition is invalid. Return a large number.
            if not found_one:
                return float('inf')
            
            return (max_r - min_r + 1) * (max_c - min_c + 1)

        # Case 1: Three horizontal strips ☰
        for i in range(1, m):
            for j in range(i + 1, m):
                area1 = get_min_area(0, 0, i - 1, n - 1)
                area2 = get_min_area(i, 0, j - 1, n - 1)
                area3 = get_min_area(j, 0, m - 1, n - 1)
                res = min(res, area1 + area2 + area3)

        # Case 2: Three vertical strips ║║║
        for i in range(1, n):
            for j in range(i + 1, n):
                area1 = get_min_area(0, 0, m - 1, i - 1)
                area2 = get_min_area(0, i, m - 1, j - 1)
                area3 = get_min_area(0, j, m - 1, n - 1)
                res = min(res, area1 + area2 + area3)

        # Case 3: One top, two bottom ⊤
        for i in range(1, m):
            for j in range(1, n):
                area1 = get_min_area(0, 0, i - 1, n - 1)
                area2 = get_min_area(i, 0, m - 1, j - 1)
                area3 = get_min_area(i, j, m - 1, n - 1)
                res = min(res, area1 + area2 + area3)

        # Case 4: One bottom, two top ⊥
        for i in range(1, m):
            for j in range(1, n):
                area1 = get_min_area(i, 0, m - 1, n - 1)
                area2 = get_min_area(0, 0, i - 1, j - 1)
                area3 = get_min_area(0, j, i - 1, n - 1)
                res = min(res, area1 + area2 + area3)
        
        # Case 5: One left, two right ⊢
        for i in range(1, n):
            for j in range(1, m):
                area1 = get_min_area(0, 0, m - 1, i - 1)
                area2 = get_min_area(0, i, j - 1, n - 1)
                area3 = get_min_area(j, i, m - 1, n - 1)
                res = min(res, area1 + area2 + area3)

        # Case 6: One right, two left ⊣
        for i in range(1, n):
            for j in range(1, m):
                area1 = get_min_area(0, i, m - 1, n - 1)
                area2 = get_min_area(0, 0, j - 1, i - 1)
                area3 = get_min_area(j, 0, m - 1, i - 1)
                res = min(res, area1 + area2 + area3)

        return res