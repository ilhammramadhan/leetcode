from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Step 1: Sort the happiness array in descending order.
        # This ensures we consider the happiest children first.
        happiness.sort(reverse=True)
        
        total_happiness_sum = 0
        
        # Step 2: Iterate k times to select the top k children
        for i in range(k):
            # Step 3: Calculate the current happiness value.
            # We subtract 'i' because at turn 'i', the value has decreased by 'i'.
            current_val = happiness[i] - i
            
            # Step 4: Check if the value is positive.
            # If current_val <= 0, adding it won't help (and we can't add negatives).
            # Since the list is sorted, if this value is <= 0, all remaining will be too.
            if current_val > 0:
                total_happiness_sum += current_val
            else:
                # Optimization: No need to check further if the best remaining is 0
                break
                
        return total_happiness_sum