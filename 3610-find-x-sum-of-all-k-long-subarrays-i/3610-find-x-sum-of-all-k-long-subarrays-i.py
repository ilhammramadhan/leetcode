from typing import List
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        answer = []
        n = len(nums)
        
        # 1. Loop through all possible windows of size k
        for i in range(n - k + 1):
            # 2. Get the current subarray (window)
            subarray = nums[i : i + k]
            
            # 3. Calculate the x-sum for this subarray and add to answer
            answer.append(self.calculate_x_sum(subarray, x))
            
        return answer

    def calculate_x_sum(self, sub: List[int], x: int) -> int:
        """Helper function to calculate the x-sum for a single subarray."""
        
        # Step 1: Count occurrences of all elements
        counts = Counter(sub)
        
        # Step 2: Sort elements. 
        # Primary key: frequency (item[1]), descending
        # Secondary key (tie-breaker): value (item[0]), descending
        # `reverse=True` handles this sorting for the (freq, val) tuple
        sorted_items = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)
        
        # Step 3: Keep only the top x most frequent elements
        # Note: If len(sorted_items) < x, this slice just takes all of them
        top_x_pairs = sorted_items[:x]
        
        # Create a set of the *values* to keep for efficient lookup
        elements_to_keep = {pair[0] for pair in top_x_pairs}
        
        # Step 4: Calculate the sum of the resulting array
        x_sum = 0
        # Iterate through the ORIGINAL subarray
        for num in sub:
            # Only add the number if it's one of the top x elements
            if num in elements_to_keep:
                x_sum += num
                
        return x_sum