import heapq

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # dist[u][r][c] = min cost to reach (r, c) using u teleports
        # We use a 1D array flattened for speed: dist[u * m * n + r * n + c]
        inf = float('inf')
        dist = [[inf] * n for _ in range(m)]
        
        # Priority Queue: (cost, r, c, teleports_used)
        pq = [(0, 0, 0, 0)]
        dist[0][0] = 0
        
        # To handle teleports in O(1), we track the best cost found so far 
        # for EACH teleport level. 
        # best_tele_out[u][val] = min cost to reach a cell with value 'val' using u teleports.
        # Since we can teleport to ANY cell with grid[nr][nc] <= grid[r][c],
        # we actually want: min_cost_to_teleport_FROM_value[u][val]
        best_from_val = [{} for _ in range(k + 1)]

        # We need a way to quickly find the min cost among all cells already reached 
        # that have a grid value >= current_grid_value.
        # We'll use a simple array since max grid value is 10,000.
        max_val = 0
        for row in grid:
            for v in row:
                max_val = max(max_val, v)
        
        # min_reach[u][v] = min cost to reach a cell with grid value >= v using u teleports
        min_reach = [[inf] * (max_val + 2) for _ in range(k + 1)]

        while pq:
            d, r, c, u = heapq.heappop(pq)
            
            if d > dist[r][c] and u == 0: # This is a simplified check
                continue

            if r == m - 1 and c == n - 1:
                return d
            
            # --- 1. Normal Moves (Cost: grid[nr][nc]) ---
            for dr, dc in [(0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_dist = d + grid[nr][nc]
                    # Note: In a real multi-layer Dijkstra, we'd check dist[u][nr][nc]
                    # For brevity and the k constraint, we focus on the teleport jump:
                    if new_dist < 1000000: # Placeholder for actual layer logic
                         pass

            # --- 2. Teleport Logic (The optimized way) ---
            # If we are at (r, c), we can be a SOURCE for a teleport to any cell with value <= grid[r][c].
            # This is hard to do forward. Instead, let's do it BACKWARD:
            # "Can I reach (r, c) via a teleport from some previous cell?"
            # This happens if min_reach[u-1][grid[r][c]] < current_dist
        
        # Re-writing to the most concise version that passes Python's overhead:
        return self.solve_layered(grid, k)

    def solve_layered(self, grid, k):
        m, n = len(grid), len(grid[0])
        # dp[u][r][c] is min cost
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 0
        
        # We iterate k+1 times. In each iteration, we run Dijkstra for normal moves,
        # then we allow one teleport to start the next iteration.
        for u in range(k + 1):
            # Dijkstra for current layer (Normal moves)
            pq = []
            for r in range(m):
                for c in range(n):
                    if dp[r][c] != float('inf'):
                        heapq.heappush(pq, (dp[r][c], r, c))
            
            while pq:
                d, r, c = heapq.heappop(pq)
                if d > dp[r][c]: continue
                for nr, nc in [(r+1, c), (r, c+1)]:
                    if nr < m and nc < n:
                        if d + grid[nr][nc] < dp[nr][nc]:
                            dp[nr][nc] = d + grid[nr][nc]
                            heapq.heappush(pq, (dp[nr][nc], nr, nc))
            
            if u == k: break
            
            # Prepare next layer via teleport:
            # New_dp[nr][nc] = min(dp[r][c]) where grid[nr][nc] <= grid[r][c]
            # To do this in O(MN), sort cells by value.
            cells = sorted([(grid[r][c], r, c) for r in range(m) for c in range(n)])
            
            suffix_min = float('inf')
            # Iterate backwards through sorted values to find the best dp[r][c] 
            # for the largest grid[r][c]
            best_at_val = {}
            curr_best = float('inf')
            for val, r, c in reversed(cells):
                curr_best = min(curr_best, dp[r][c])
                best_at_val[val] = curr_best
            
            new_dp = [row[:] for row in dp]
            for r in range(m):
                for c in range(n):
                    # We can teleport to (r, c) from any cell with value >= grid[r][c]
                    new_dp[r][c] = min(new_dp[r][c], best_at_val[grid[r][c]])
            dp = new_dp
            
        return dp[m-1][n-1]