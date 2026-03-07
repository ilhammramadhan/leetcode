class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        # Step 2: Double the string to simulate all Type-1 operations
        s = s + s 
        
        # Step 1: Create the two ideal alternating targets of length 2N
        target1 = ""
        target2 = ""
        for i in range(len(s)):
            # target1 = "101010..."
            target1 += '1' if i % 2 == 0 else '0'
            # target2 = "010101..."
            target2 += '0' if i % 2 == 0 else '1'
            
        ans = float('inf') # Set initial minimum to infinity
        diff1, diff2 = 0, 0
        l = 0 # Left pointer for our sliding window
        
        # Step 3: Slide the right pointer across the doubled string
        for r in range(len(s)):
            # Add the new character's contribution to our difference counts
            if s[r] != target1[r]:
                diff1 += 1
            if s[r] != target2[r]:
                diff2 += 1
                
            # If our window has grown larger than the original string length N, 
            # we need to shrink it from the left.
            if r - l + 1 > n:
                # Remove the left character's contribution
                if s[l] != target1[l]:
                    diff1 -= 1
                if s[l] != target2[l]:
                    diff2 -= 1
                # Slide the left pointer forward
                l += 1
                
            # Whenever our window is exactly size N, we check if we found a new minimum
            if r - l + 1 == n:
                ans = min(ans, diff1, diff2)
                
        return ans