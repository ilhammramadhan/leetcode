class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
                continue
            
            # We need to find the lowest bit that is 0 
            # and flip the bit to its right.
            # Effectively, find the length of the trailing sequence of 1s.
            
            # bit will track the position of the 1 we want to flip to 0
            bit = 1
            # While the bit at this position is 1, move to the next bit
            # (n >> i) & 1 checks if the i-th bit is 1
            while (n >> bit) & 1:
                bit += 1
            
            # The bit we want to flip to 0 is at (bit - 1)
            # Subtracting 2^(bit-1) is the same as flipping that bit to 0
            ans.append(n - (1 << (bit - 1)))
            
        return ans