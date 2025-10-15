from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # Step 1: Calculate lengths of increasing subarrays ENDING at index i
        # This is done with a forward pass.
        dp_ending = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp_ending[i] = dp_ending[i-1] + 1
        
        # Step 2: Calculate lengths of increasing subarrays STARTING at index i
        # This is done with a backward pass.
        dp_starting = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                dp_starting[i] = dp_starting[i+1] + 1

        # Step 3: Iterate through all possible split points and find the max k
        max_k = 0
        # A split occurs between index i-1 and i
        for i in range(1, n):
            # For a given split, the max possible common length is the minimum
            # of the length of the subarray ending before the split and the
            # length of the subarray starting after the split.
            possible_k = min(dp_ending[i-1], dp_starting[i])
            max_k = max(max_k, possible_k)
            
        return max_k