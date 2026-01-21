class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
                continue
            
            # We look for the first '0' bit from the right.
            # In an odd number, the sequence ends in one or more 1s.
            # Example: 13 is 1101. 
            # We want to find the lowest bit that, when set to 0, 
            # still results in n when OR'd with (ans + 1).
            
            for i in range(1, 32):
                # Check if the i-th bit is 0
                if not (n & (1 << i)):
                    # The bit to flip is the (i-1)-th bit
                    # We use XOR to flip that specific bit to 0
                    ans.append(n ^ (1 << (i - 1)))
                    break
        return ans