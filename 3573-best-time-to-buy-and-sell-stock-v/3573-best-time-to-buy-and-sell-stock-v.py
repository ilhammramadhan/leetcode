class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        
        # Edge case: If no prices or k is 0, no profit can be made.
        if n < 2 or k == 0:
            return 0
        
        # We need to track profit states for up to k transactions.
        # idle[j]: Max profit having completed exactly j transactions.
        # active_normal[j]: Max profit having completed j transactions AND holding a buy position (waiting to sell).
        # active_short[j]: Max profit having completed j transactions AND holding a short position (waiting to buy back).
        
        # Initialization
        # We use -inf to represent unreachable states initially.
        idle = [-float('inf')] * (k + 1)
        active_normal = [-float('inf')] * (k + 1)
        active_short = [-float('inf')] * (k + 1)
        
        # Base case: Before any days pass, 0 transactions done = 0 profit.
        idle[0] = 0
        
        for p in prices:
            # We create new arrays to hold values for the current day to ensure
            # we don't use data from the *current* day to start new trades (strict disjoint constraint).
            new_idle = idle[:]
            new_active_normal = active_normal[:]
            new_active_short = active_short[:]
            
            for j in range(k):
                # --- STARTING TRANSACTIONS ---
                
                # 1. Try to start a Normal transaction (Buy)
                # We use idle[j] from yesterday. Cost is p.
                if idle[j] != -float('inf'):
                    new_active_normal[j] = max(active_normal[j], idle[j] - p)
                
                # 2. Try to start a Short transaction (Sell Short)
                # We use idle[j] from yesterday. Gain is p.
                if idle[j] != -float('inf'):
                    new_active_short[j] = max(active_short[j], idle[j] + p)

                # --- FINISHING TRANSACTIONS ---
                # These complete the (j+1)th transaction
                
                # 3. Try to close a Normal transaction (Sell)
                # Profit = value of holding normal + p
                if active_normal[j] != -float('inf'):
                    new_idle[j+1] = max(new_idle[j+1], active_normal[j] + p)
                
                # 4. Try to close a Short transaction (Buy Back)
                # Profit = value of holding short - p
                if active_short[j] != -float('inf'):
                    new_idle[j+1] = max(new_idle[j+1], active_short[j] - p)
            
            # Update the main arrays for the next day
            idle = new_idle
            active_normal = new_active_normal
            active_short = new_active_short
            
        # The answer is the maximum profit found in any 'idle' state 
        # (meaning all transactions are closed).
        return max(idle)