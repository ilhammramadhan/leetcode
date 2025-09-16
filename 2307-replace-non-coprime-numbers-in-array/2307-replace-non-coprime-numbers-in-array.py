class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        # res will act as our stack
        res = []
        
        # Iterate through each number in the input array
        for num in nums:
            # Add the current number to our result list
            res.append(num)
            
            # Keep merging the last two elements as long as they are non-coprime
            # This loop handles cases where a new LCM creates another non-coprime pair with the element before it
            while len(res) > 1 and math.gcd(res[-1], res[-2]) > 1:
                # Pop the last two non-coprime numbers
                y = res.pop()
                x = res.pop()
                
                # Calculate their LCM using the formula: (a * b) / gcd(a, b)
                # Use integer division //
                lcm = (x * y) // math.gcd(x, y)
                
                # Append the new LCM value back to the list
                res.append(lcm)
                
        return res