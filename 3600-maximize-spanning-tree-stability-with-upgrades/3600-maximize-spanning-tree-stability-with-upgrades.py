from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.num_sets = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.num_sets -= 1
            return True
        return False

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # 1. Check if mandatory edges form a cycle
        dsu_must = DSU(n)
        must_edges = []
        for u, v, s, m in edges:
            if m == 1:
                if not dsu_must.union(u, v):
                    return -1 # Cycle in mandatory edges
                must_edges.append((u, v, s))
        
        if len(must_edges) > n - 1:
            return -1

        def check(target_stability):
            dsu = DSU(n)
            upgrades_used = 0
            edges_count = 0
            
            # 1. Add all mandatory edges (must be >= target)
            for u, v, s in must_edges:
                if s < target_stability:
                    return False
                dsu.union(u, v)
                edges_count += 1
            
            # 2. Add optional edges that satisfy target WITHOUT upgrade
            optional_no_up = []
            optional_with_up = []
            for u, v, s, m in edges:
                if m == 0:
                    if s >= target_stability:
                        optional_no_up.append((u, v))
                    elif 2 * s >= target_stability:
                        optional_with_up.append((u, v))
            
            for u, v in optional_no_up:
                if dsu.union(u, v):
                    edges_count += 1
            
            # 3. Add optional edges that satisfy target WITH upgrade
            for u, v in optional_with_up:
                if upgrades_used < k:
                    if dsu.union(u, v):
                        upgrades_used += 1
                        edges_count += 1
            
            return edges_count == n - 1

        # Binary search for the maximum stability
        low = 0
        high = 2 * max(edge[2] for edge in edges)
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans