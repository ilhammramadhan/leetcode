import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        # 1. Build Adjacency Lists
        adj = defaultdict(list)
        rev_adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            rev_adj[v].append((u, w))
            
        # 2. Dijkstra setup
        # dist[i] stores the min cost to reach node i
        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]  # (cost, node)
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            if u == n - 1:
                return d
            
            # Option A: Move along normal edges
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
            
            # Option B: Use the switch at node u 
            # Reverse an incoming edge (v -> u) to (u -> v)
            for v, w in rev_adj[u]:
                new_cost = dist[u] + 2 * w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
                    
        return dist[n-1] if dist[n-1] != float('inf') else -1