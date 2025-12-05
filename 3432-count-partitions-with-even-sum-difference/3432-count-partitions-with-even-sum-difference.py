class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. Get the total sum of the array
        total_sum = sum(nums)
        
        left_sum = 0
        count = 0
        
        # 2. Iterate from index 0 to n-2
        # We use n-1 as the range limit because range is exclusive
        for i in range(n - 1):
            
            # Add current element to left side
            left_sum += nums[i]
            
            # Calculate right side based on total
            right_sum = total_sum - left_sum
            
            # 3. Check if difference is even
            if (left_sum - right_sum) % 2 == 0:
                count += 1
                
        return count