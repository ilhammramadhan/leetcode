from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def can_cross(day):
            # 1. Initialize the grid for this specific day
            # 0 = land, 1 = water
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1
            
            # 2. BFS Setup: Find all starting points (land in the top row)
            queue = deque()
            visited = set()
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    visited.add((0, c))
            
            # 3. Standard BFS traversal
            while queue:
                r, c = queue.popleft()
                
                # If we reach the last row, we found a path!
                if r == row - 1:
                    return True
                
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and \
                       grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            return False

        # Binary Search for the last possible day
        left, right = 1, len(cells)
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if can_cross(mid):
                ans = mid    # This day works, try to find a later one
                left = mid + 1
            else:
                right = mid - 1 # Too much water, try an earlier day
                
        return ans