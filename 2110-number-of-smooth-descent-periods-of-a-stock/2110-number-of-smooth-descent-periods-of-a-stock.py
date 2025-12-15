from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # Edge case: if the list is empty (though constraints say length >= 1)
        if not prices:
            return 0
        
        # Initialize total count and current streak length
        # We count index 0 immediately as 1 period.
        total_periods = 1
        current_streak = 1
        
        # Iterate starting from the second element (index 1)
        for i in range(1, len(prices)):
            # Check if current price is exactly 1 less than previous
            if prices[i] == prices[i - 1] - 1:
                current_streak += 1
            else:
                # Reset streak if the condition is broken
                current_streak = 1
            
            # Add the number of periods ending at this index to the total
            total_periods += current_streak
            
        return total_periods