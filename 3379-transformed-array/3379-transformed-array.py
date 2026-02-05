class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        
        # Iterate through each index of the array
        for i in range(n):
            # Calculate the movement steps directly from the value
            steps = nums[i]
            
            # Calculate the new index using modulo for circular wrapping
            # (i + steps) handles both positive (right) and negative (left) movement
            target_index = (i + steps) % n
            
            # Append the value found at the target index to our result
            result.append(nums[target_index])
            
        return result