class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # We need the math.gcd function
        import math
        
        n = len(nums)
        
        # --- Scenario 1: A '1' already exists ---
        ones = nums.count(1)
        if ones > 0:
            # Total ops = (elements to change) = n - (elements that are already 1)
            return n - ones
            
        # --- Scenarios 2 & 3: No '1's exist ---
        
        # We must find the cost to CREATE the first 1 (Phase A)
        min_ops_to_create_one = float('inf')
        
        # Check every possible subarray
        for i in range(n):
            g = nums[i] # g = gcd(nums[i...j])
            for j in range(i + 1, n):
                g = math.gcd(g, nums[j])
                
                if g == 1:
                    # Found a subarray nums[i...j] with gcd=1
                    # Length k = (j - i + 1)
                    # Ops to create 1 = k - 1 = (j - i)
                    ops = (j - i)
                    min_ops_to_create_one = min(min_ops_to_create_one, ops)
                    break # Found shortest subarray starting at i

        # --- Handle Results ---
        
        # Scenario 3: Impossible
        if min_ops_to_create_one == float('inf'):
            # We looped through everything and never found a subarray with gcd=1
            return -1
            
        # Scenario 2: Possible
        else:
            # Total Ops = (Phase A: Ops to create 1) + (Phase B: Ops to propagate 1)
            return min_ops_to_create_one + (n - 1)