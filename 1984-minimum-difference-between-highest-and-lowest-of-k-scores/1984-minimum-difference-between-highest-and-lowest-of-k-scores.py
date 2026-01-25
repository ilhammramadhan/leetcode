class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the scores
        nums.sort()
        
        # Step 2: Initialize min_diff with a very large value
        # Or just handle the k=1 case early
        min_diff = float('inf')
        
        # Step 3: Iterate through the array with a window of size k
        # We stop at len(nums) - k to ensure the window stays in bounds
        for i in range(len(nums) - k + 1):
            # Calculate difference between the end and start of the window
            current_diff = nums[i + k - 1] - nums[i]
            
            # Update min_diff if we found a smaller one
            min_diff = min(min_diff, current_diff)
            
        return min_diff