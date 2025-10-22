from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        
        n = len(nums)
        
        # --- Step 1: Create the set of candidate targets ---
        # The optimal target 'T' must be at one of the "boundary" points:
        # num, num - k, or num + k.
        candidates = set()
        for num in nums:
            candidates.add(num)
            candidates.add(num - k)
            candidates.add(num + k)
            
        # --- Step 2: Sort nums for binary search (O(N log N)) ---
        nums.sort()
        
        max_freq = 0
        
        # --- Step 3: Iterate through all O(N) candidates ---
        for target in candidates:
            
            # --- Step 4: Find e (count of EQUAL) (O(log N)) ---
            idx_left_e = bisect_left(nums, target)
            idx_right_e = bisect_right(nums, target)
            e = idx_right_e - idx_left_e
            
            # --- Step 5: Find c (count of CHANGEABLE) (O(log N)) ---
            idx_left_range = bisect_left(nums, target - k)
            idx_right_range = bisect_right(nums, target + k)
            total_in_range = idx_right_range - idx_left_range
            c = total_in_range - e
            
            # --- Step 6: Calculate frequency for this target (THE CORRECT LOGIC) ---
            
            # We get 'e' points guaranteed, as these elements are already
            # the target and can be put in *either* the U or M group (by adding 0).
            freq_from_equal = e
            
            # We get additional points by using our operations to "buy"
            # elements from the 'c' group.
            freq_from_changeable = min(c, numOperations)
            
            # The total frequency is the sum.
            current_freq = freq_from_equal + freq_from_changeable
            
            # --- Step 7: Update the overall maximum ---
            max_freq = max(max_freq, current_freq)
            
        return max_freq