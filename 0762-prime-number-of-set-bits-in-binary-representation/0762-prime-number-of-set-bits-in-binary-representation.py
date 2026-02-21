class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Define the primes possible within 20 bits (since 10^6 < 2^20)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        count = 0
        
        # Iterate through the inclusive range
        for num in range(left, right + 1):
            # Calculate set bits using the built-in bit_count()
            # If you are on an older Python version, use bin(num).count('1')
            set_bits = num.bit_count()
            
            # Check if the bit count is in our prime set
            if set_bits in primes:
                count += 1
                
        return count