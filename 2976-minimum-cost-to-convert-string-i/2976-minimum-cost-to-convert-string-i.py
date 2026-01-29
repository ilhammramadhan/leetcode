from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # 1. Initialize the distance matrix with infinity
        # Since there are only 26 lowercase English letters
        dist = [[float('inf')] * 26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
            
        # 2. Map 'a'-'z' to 0-25 and fill initial transformation costs
        for src, dst, c in zip(original, changed, cost):
            u, v = ord(src) - ord('a'), ord(dst) - ord('a')
            dist[u][v] = min(dist[u][v], c)
            
        # 3. Floyd-Warshall: Find the shortest path between all pairs
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # 4. Calculate total cost for the strings
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            
            u, v = ord(s) - ord('a'), ord(t) - ord('a')
            step_cost = dist[u][v]
            
            if step_cost == float('inf'):
                return -1
            
            total_cost += step_cost
            
        return int(total_cost)