from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # 1. Build Adjacency List
        # Nodes are 1-based, so we make the array size n + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            adj[u].append(v)
        
        # Helper function to merge a list of DP tables (Knapsack convolution)
        # dp_list: list of arrays, where each array maps cost -> max_profit
        def merge_dps(dp_list):
            # Initialize with base state: 0 cost, 0 profit. 
            # -float('inf') indicates an unreachable cost.
            current_dp = [-float('inf')] * (budget + 1)
            current_dp[0] = 0
            
            for child_dp in dp_list:
                # Temporary array for the new merged state
                new_dp = [-float('inf')] * (budget + 1)
                
                # Try to combine every valid cost in current_dp with every valid cost in child_dp
                # Optimization: Iterate only valid ranges to speed up
                for b1 in range(budget + 1):
                    if current_dp[b1] == -float('inf'): continue
                    
                    for b2 in range(budget - b1 + 1):
                        if child_dp[b2] == -float('inf'): continue
                        
                        # Maximize profit for the combined cost
                        if current_dp[b1] + child_dp[b2] > new_dp[b1 + b2]:
                            new_dp[b1 + b2] = current_dp[b1] + child_dp[b2]
                
                current_dp = new_dp
            return current_dp

        # 2. DFS Function
        def dfs(u):
            # Gather results from all children
            child_res_if_u_buys = []    # Children's tables if u buys (they get discount)
            child_res_if_u_skips = []   # Children's tables if u skips (they pay full)
            
            for v in adj[u]:
                res = dfs(v)
                child_res_if_u_skips.append(res[0]) # res[0] is 'parent didn't buy'
                child_res_if_u_buys.append(res[1])  # res[1] is 'parent bought'
            
            # Merge children's results into consolidated tables
            merged_buy_table = merge_dps(child_res_if_u_buys)
            merged_skip_table = merge_dps(child_res_if_u_skips)
            
            # Prepare the two result tables for node u
            # dp_no_parent_buy: u pays full price
            # dp_parent_buy: u pays discounted price
            dp_no_parent_buy = [-float('inf')] * (budget + 1)
            dp_parent_buy = [-float('inf')] * (budget + 1)
            
            # --- Logic for dp_no_parent_buy ---
            
            # Option A: u Skips (Cost 0, Profit 0)
            # If u skips, we take the best profits from children assuming u skipped
            for b in range(budget + 1):
                if merged_skip_table[b] != -float('inf'):
                    dp_no_parent_buy[b] = max(dp_no_parent_buy[b], merged_skip_table[b])
            
            # Option B: u Buys (Full Cost)
            # If u buys, we take best profits from children assuming u bought, then add u's stats
            cost = present[u-1]
            profit = future[u-1] - cost
            if cost <= budget:
                for b in range(budget - cost + 1):
                    if merged_buy_table[b] != -float('inf'):
                        dp_no_parent_buy[b + cost] = max(dp_no_parent_buy[b + cost], merged_buy_table[b] + profit)
            
            # --- Logic for dp_parent_buy ---
            
            # Option A: u Skips (Cost 0, Profit 0)
            # Even if parent bought, u can choose to skip. Children see u as skipped.
            for b in range(budget + 1):
                if merged_skip_table[b] != -float('inf'):
                    dp_parent_buy[b] = max(dp_parent_buy[b], merged_skip_table[b])

            # Option B: u Buys (Discounted Cost)
            # Parent bought, so u buys at half price. Children see u as bought.
            cost_disc = present[u-1] // 2
            profit_disc = future[u-1] - cost_disc
            if cost_disc <= budget:
                for b in range(budget - cost_disc + 1):
                    if merged_buy_table[b] != -float('inf'):
                        dp_parent_buy[b + cost_disc] = max(dp_parent_buy[b + cost_disc], merged_buy_table[b] + profit_disc)
            
            # Return tuple: (result if u's parent didn't buy, result if u's parent bought)
            return dp_no_parent_buy, dp_parent_buy

        # 3. Execution
        # Get result from root (CEO). CEO has no parent, so we take index 0 (no parent buy).
        final_dp = dfs(1)[0]
        
        # The answer is the maximum profit found in the final DP table (ignoring -inf)
        return max(0, max(final_dp))