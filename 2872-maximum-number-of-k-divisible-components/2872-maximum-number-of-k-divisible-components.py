from collections import defaultdict
from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # 1. Build Adjacency List
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        self.components_count = 0
        
        # 2. DFS Helper Function
        def dfs(node, parent):
            # Start with the value of the current node
            total_sum = values[node]
            
            # Traverse children
            for child in adj[node]:
                if child != parent:
                    # Add the sum returned by the child
                    total_sum += dfs(child, node)
            
            # 3. Check Divisibility
            if total_sum % k == 0:
                self.components_count += 1
                # If this component is valid, we "cut" it off.
                # Returning 0 effectively removes it from the parent's calculation.
                return 0
            
            # Otherwise, pass the sum up to the parent
            return total_sum

        # 4. Start DFS from root (node 0)
        dfs(0, -1)
        
        return self.components_count