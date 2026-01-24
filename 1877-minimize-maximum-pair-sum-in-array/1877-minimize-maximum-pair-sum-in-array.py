class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # 1. Sort the array to organize numbers from smallest to largest
        nums.sort()
        
        max_sum = 0
        n = len(nums)
        
        # 2. Use a loop to pair the i-th smallest with the i-th largest
        # We only need to go up to n // 2 because we are processing two elements at once
        for i in range(n // 2):
            # Calculate the sum of the current pair
            current_pair_sum = nums[i] + nums[n - 1 - i]
            
            # 3. Update max_sum if the current pair is larger than what we've seen
            if current_pair_sum > max_sum:
                max_sum = current_pair_sum
                
        return max_sum