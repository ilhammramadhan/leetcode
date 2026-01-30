import math

class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        n = len(source)
        
        # --- Step 1: Map all unique strings to integer IDs ---
        # We need this to build our adjacency matrix for Floyd-Warshall.
        nodes = set(original) | set(changed)
        str_to_id = {s: i for i, s in enumerate(nodes)}
        num_nodes = len(nodes)
        
        # --- Step 2: Build the Graph and run Floyd-Warshall ---
        # Initialize distance matrix with infinity
        inf = float('inf')
        dist = [[inf] * num_nodes for _ in range(num_nodes)]
        
        # Distance to self is always 0
        for i in range(num_nodes):
            dist[i][i] = 0
            
        # Fill initial costs from input
        for src, dst, c in zip(original, changed, cost):
            u, v = str_to_id[src], str_to_id[dst]
            dist[u][v] = min(dist[u][v], c)
            
        # Floyd-Warshall Algorithm to find All-Pairs Shortest Path
        for k in range(num_nodes):
            for i in range(num_nodes):
                if dist[i][k] == inf: continue # Optimization
                for j in range(num_nodes):
                    if dist[k][j] == inf: continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # --- Step 3: Build a Trie for efficient substring matching ---
        # We only need to match strings that exist in 'original'
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.id = -1 # Valid ID if this node marks the end of a string in 'original'

        root = TrieNode()
        for s in original:
            curr = root
            for char in s:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.id = str_to_id[s] # Mark this path as a valid 'original' string

        # --- Step 4: Dynamic Programming ---
        # dp[i] = min cost to convert source[:i] to target[:i]
        dp = [inf] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == inf:
                continue
            
            # Case A: Characters match directly (Cost 0)
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            
            # Case B: Perform a substring conversion starting at i
            # Use Trie to find all substrings starting at i that exist in 'original'
            curr = root
            for k in range(i, n):
                char = source[k]
                if char not in curr.children:
                    break # No original string matches this prefix
                curr = curr.children[char]
                
                # If we found a valid string from 'original'
                if curr.id != -1:
                    u = curr.id
                    # We have source[i:k+1]. Now check target[i:k+1].
                    # Note: slicing strings inside the loop is okay here because
                    # we only do it when we find a match in the Trie (rare event).
                    target_sub = target[i : k+1]
                    
                    if target_sub in str_to_id:
                        v = str_to_id[target_sub]
                        if dist[u][v] != inf:
                            dp[k+1] = min(dp[k+1], dp[i] + dist[u][v])
                            
        # Final result
        res = dp[n]
        return res if res != inf else -1