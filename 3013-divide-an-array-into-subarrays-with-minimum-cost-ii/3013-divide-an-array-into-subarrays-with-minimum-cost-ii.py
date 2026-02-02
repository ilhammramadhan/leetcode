from sortedcontainers import SortedList
from typing import List

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        need = k - 1  # We need to pick k-1 indices (excluding index 0)
        
        top = SortedList()      # k-1 smallest elements: (value, index)
        rest = SortedList()     # Remaining elements in window
        top_sum = 0
        
        def add(val, idx):
            """Add element to appropriate set, maintain top has smallest k-1"""
            nonlocal top_sum
            elem = (val, idx)
            
            if len(top) < need:
                # top isn't full yet, just add
                top.add(elem)
                top_sum += val
            elif elem < top[-1]:
                # New elem is smaller than largest in top
                # Swap: move largest from top to rest, add new elem to top
                out = top.pop()
                top_sum -= out[0]
                rest.add(out)
                top.add(elem)
                top_sum += val
            else:
                # New elem is larger, goes to rest
                rest.add(elem)
        
        def remove(val, idx):
            """Remove element, refill top from rest if needed"""
            nonlocal top_sum
            elem = (val, idx)
            
            if elem in top:
                top.remove(elem)
                top_sum -= val
                # Refill top from rest (take smallest from rest)
                if rest:
                    new_elem = rest.pop(0)  # Smallest in rest
                    top.add(new_elem)
                    top_sum += new_elem[0]
            else:
                rest.remove(elem)
        
        # Initialize: first window covers indices [1, 1+dist]
        for i in range(1, min(2 + dist, n)):
            add(nums[i], i)
        
        min_cost = top_sum
        
        # Slide window: left boundary goes from 1 to (n-k+1)
        # When left = L, window is [L, L+dist]
        for left in range(2, n - k + 2):
            # Element at (left-1) leaves the window
            remove(nums[left - 1], left - 1)
            
            # Element at (left+dist) enters the window (if valid)
            new_right = left + dist
            if new_right < n:
                add(nums[new_right], new_right)
            
            # Update answer
            if len(top) == need:
                min_cost = min(min_cost, top_sum)
        
        return nums[0] + min_cost