import collections
from typing import List

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Arrays to store results from DFS
        subtree_xor = [-1] * n
        entry = [-1] * n
        exit_t = [-1] * n
        # Use a list for the timer to pass it by reference in the recursive DFS
        timer = [0]

        # Step 1: DFS to compute subtree XORs and entry/exit times for ancestry checks
        def dfs(u: int, p: int):
            entry[u] = timer[0]
            timer[0] += 1
            
            current_xor = nums[u]
            for v in adj[u]:
                if v != p:
                    current_xor ^= dfs(v, u)
            
            subtree_xor[u] = current_xor
            exit_t[u] = timer[0]
            timer[0] += 1
            return subtree_xor[u]

        # Start DFS from an arbitrary root (node 0)
        dfs(0, -1)
        total_xor = subtree_xor[0]
        min_score = float('inf')

        # Helper function to check if u is an ancestor of v in O(1)
        def is_ancestor(u: int, v: int) -> bool:
            return entry[u] <= entry[v] and exit_t[v] <= exit_t[u]

        # Step 2 & 3: Iterate over all pairs of edges (by choosing nodes i and j) and calculate score
        for i in range(1, n):
            for j in range(i + 1, n):
                xor_i = subtree_xor[i]
                xor_j = subtree_xor[j]
                
                a, b, c = 0, 0, 0

                # Case 1: Subtree 'i' contains subtree 'j'
                if is_ancestor(i, j):
                    a = xor_j
                    b = xor_i ^ xor_j
                    c = total_xor ^ xor_i
                # Case 2: Subtree 'j' contains subtree 'i'
                elif is_ancestor(j, i):
                    a = xor_i
                    b = xor_j ^ xor_i
                    c = total_xor ^ xor_j
                # Case 3: Disjoint subtrees
                else:
                    a = xor_i
                    b = xor_j
                    c = total_xor ^ xor_i ^ xor_j

                # Step 4: Update the minimum score
                score = max(a, b, c) - min(a, b, c)
                min_score = min(min_score, score)

        return min_score