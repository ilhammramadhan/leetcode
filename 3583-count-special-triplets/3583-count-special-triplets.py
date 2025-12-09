from collections import Counter
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        # 1. Initialize the Right Map with all frequencies
        right_map = Counter(nums)
        
        # 2. Initialize the Left Map (empty)
        left_map = Counter()
        
        total_triplets = 0
        
        # 3. Iterate through the array treating each element as the middle (j)
        for num in nums:
            # Remove current number from right_map because it is now the center
            right_map[num] -= 1
            
            # The target for i and k is (num * 2)
            target = num * 2
            
            # If target exists in both maps, calculate combinations
            # We use .get(target, 0) to avoid errors if the key doesn't exist
            left_count = left_map[target]
            right_count = right_map[target]
            
            if left_count > 0 and right_count > 0:
                total_triplets += (left_count * right_count)
                total_triplets %= MOD
            
            # Add current number to left_map for the next iteration
            left_map[num] += 1
            
        return total_triplets