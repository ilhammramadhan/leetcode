class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones_count = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '1':
                ones_count += 1
                i += 1
            else:
                # We found a '0' (start of a gap)
                # Add current accumulated '1's to the answer
                ans += ones_count
                
                # Fast-forward 'i' to skip all consecutive zeros
                # because '100' is treated as 1 jump, not 2.
                while i < n and s[i] == '0':
                    i += 1
                    
        return ans