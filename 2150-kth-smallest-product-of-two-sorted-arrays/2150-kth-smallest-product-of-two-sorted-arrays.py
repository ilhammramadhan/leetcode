import bisect
from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        def count_le(x: int) -> int:
            """
            Counts products <= x using a logically simple O(N*logM) approach.
            """
            count = 0
            m = len(nums2)
            for n1 in nums1:
                if n1 == 0:
                    if x >= 0:
                        count += m
                elif n1 > 0:
                    # We need n2 <= x / n1.
                    # bisect_right finds the insertion point for target, which is the count of elements <= target.
                    target = x / n1
                    count += bisect.bisect_right(nums2, target)
                else: # n1 < 0
                    # We need n2 >= x / n1 (inequality flips).
                    # bisect_left finds the index of the first element >= target.
                    # The count is all elements from that index onwards.
                    target = x / n1
                    count += m - bisect.bisect_left(nums2, target)
            return count

        # Main binary search logic
        # The range of products can be from -10^10 to 10^10.
        low = -10**10 - 1
        high = 10**10 + 1
        ans = high

        while low <= high:
            mid = (low + high) // 2
            
            # If the number of products <= mid is at least k,
            # then mid is a potential answer, and we try to find a smaller one.
            if count_le(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                # Otherwise, mid is too small.
                low = mid + 1
        
        return ans