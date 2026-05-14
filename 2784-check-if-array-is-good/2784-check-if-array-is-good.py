from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # Step 1: Calculate 'n' based on the length of the array
        n = len(nums) - 1
        
        # Step 2: Build the expected base[n] array
        # list(range(1, n)) creates [1, 2, ..., n-1]
        # + [n, n] appends the two occurrences of n at the end
        expected = list(range(1, n)) + [n, n]
        
        # Step 3 & 4: Sort the input array and compare
        return sorted(nums) == expected