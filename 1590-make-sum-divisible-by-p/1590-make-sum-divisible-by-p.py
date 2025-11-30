class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # 1. Calculate total sum and target remainder
        total_sum = sum(nums)
        target = total_sum % p
        
        # Edge case: If already divisible, remove nothing
        if target == 0:
            return 0
        
        # 2. Map to store { remainder : most_recent_index }
        # We start with {0: -1} to handle subarrays starting at index 0
        mod_map = {0: -1}
        
        current_sum = 0
        min_len = len(nums)
        
        for i, num in enumerate(nums):
            current_sum += num
            current_mod = current_sum % p
            
            # 3. Calculate the remainder we need to have seen previously
            # The logic: (current_mod - previous_mod) % p == target
            # Therefore: previous_mod == (current_mod - target) % p
            needed = (current_mod - target) % p
            
            # 4. If we have seen this 'needed' remainder before
            if needed in mod_map:
                subarray_len = i - mod_map[needed]
                min_len = min(min_len, subarray_len)
            
            # 5. Store current remainder and index
            mod_map[current_mod] = i
            
        # 6. Final validation
        # If min_len is still the size of the whole array, return -1 (not allowed to remove all)
        return min_len if min_len < len(nums) else -1