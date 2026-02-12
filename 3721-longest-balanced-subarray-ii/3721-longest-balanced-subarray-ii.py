import sys

# Increase recursion depth for deep Segment Tree operations
sys.setrecursionlimit(200000)

class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Segment Tree Arrays
        # mins/maxs store the minimum/maximum value in a range
        # lazy stores the pending updates to be pushed down
        self.mins = [0] * (4 * n)
        self.maxs = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        
        last_pos = {}
        max_len = 0
        
        for j, num in enumerate(nums):
            # Determine contribution: Odd = +1, Even = -1
            val = 1 if num % 2 != 0 else -1
            
            # Find the range of start indices (i) for which this number is 'new'
            # It is new for any window starting after its previous occurrence.
            prev = last_pos.get(num, -1)
            start_update = prev + 1
            
            # Update the segment tree for range [start_update, j]
            if start_update <= j:
                self.update(0, 0, n - 1, start_update, j, val)
            
            # Update the last position tracker
            last_pos[num] = j
            
            # Query the tree: Find the leftmost index i in [0, j] where value is 0
            # We search in range [0, j] because valid subarrays must end at j
            idx = self.query_first_zero(0, 0, n - 1, 0, j)
            
            if idx != -1:
                current_len = j - idx + 1
                if current_len > max_len:
                    max_len = current_len
                    
        return max_len

    def push(self, node):
        """Push lazy updates to children."""
        if self.lazy[node] != 0:
            lz = self.lazy[node]
            mid = node * 2
            
            self.lazy[2 * node + 1] += lz
            self.mins[2 * node + 1] += lz
            self.maxs[2 * node + 1] += lz
            
            self.lazy[2 * node + 2] += lz
            self.mins[2 * node + 2] += lz
            self.maxs[2 * node + 2] += lz
            
            self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        """Range add val to [l, r]."""
        if l > end or r < start:
            return
        
        if l <= start and end <= r:
            self.lazy[node] += val
            self.mins[node] += val
            self.maxs[node] += val
            return
        
        self.push(node)
        mid = (start + end) // 2
        self.update(2 * node + 1, start, mid, l, r, val)
        self.update(2 * node + 2, mid + 1, end, l, r, val)
        
        self.mins[node] = min(self.mins[2 * node + 1], self.mins[2 * node + 2])
        self.maxs[node] = max(self.maxs[2 * node + 1], self.maxs[2 * node + 2])

    def query_first_zero(self, node, start, end, l, r):
        """Find the smallest index in [l, r] with value 0."""
        # Check if range overlaps
        if l > end or r < start:
            return -1
        
        # Optimization: If 0 is not in the range of values [min, max], skip
        if self.mins[node] > 0 or self.maxs[node] < 0:
            return -1
            
        # Leaf node check
        if start == end:
            return start if self.mins[node] == 0 else -1
        
        self.push(node)
        mid = (start + end) // 2
        
        # Try left child first (to find smallest index)
        res = self.query_first_zero(2 * node + 1, start, mid, l, r)
        if res != -1:
            return res
            
        # If not found in left, try right
        return self.query_first_zero(2 * node + 2, mid + 1, end, l, r)