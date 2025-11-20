from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort intervals
        # Primary key: End time ascending (x[1])
        # Secondary key: Start time descending (-x[0])
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # Step 2: Initialize variables
        # p1 is the second-to-last number added
        # p2 is the last number added
        # We start them at -1 since constraints say starts are >= 0
        p1, p2 = -1, -1
        res = 0
        
        # Step 3: Iterate through intervals
        for start, end in intervals:
            
            # Case A: No overlap
            # The interval starts after our current largest point
            if start > p2:
                res += 2
                p2 = end
                p1 = end - 1
            
            # Case B: One overlap
            # The interval contains p2, but starts after p1
            elif start > p1:
                res += 1
                p1 = p2  # The old max becomes the 2nd max
                p2 = end # The new max is the end of current interval
            
            # Case C: Two overlaps (start <= p1)
            # Both p1 and p2 are inside [start, end]
            # We do nothing, interval is already satisfied.
            
        return res