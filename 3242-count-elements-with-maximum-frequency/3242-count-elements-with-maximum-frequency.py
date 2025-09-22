from collections import Counter
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Step 1: Count the frequency of each number.
        # Counter is a special dictionary that does this for us.
        # For [1,2,2,3,1,4], freq_counts becomes Counter({1: 2, 2: 2, 3: 1, 4: 1})
        freq_counts = Counter(nums)
        
        # Check if the list is empty, if so, the max frequency is 0.
        if not freq_counts:
            return 0
        
        # Step 2: Find the maximum frequency.
        # .values() gives us all the counts: [2, 2, 1, 1]
        # max() finds the highest value, which is 2.
        max_freq = max(freq_counts.values())
        
        # Step 3: Sum the frequencies of elements with the maximum frequency.
        total_frequency = 0
        for freq in freq_counts.values():
            # If a number's frequency is equal to the max frequency...
            if freq == max_freq:
                # ...add that frequency to the total.
                total_frequency += freq
                
        return total_frequency