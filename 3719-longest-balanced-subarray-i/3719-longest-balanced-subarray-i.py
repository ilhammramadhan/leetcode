class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        
        # Iterate through every possible starting position of the subarray
        for i in range(n):
            even_set = set()
            odd_set = set()
            
            # Iterate through every possible ending position
            for j in range(i, n):
                # Add current number to the appropriate set
                if nums[j] % 2 == 0:
                    even_set.add(nums[j])
                else:
                    odd_set.add(nums[j])
                
                # Check if distinct even count equals distinct odd count
                if len(even_set) == len(odd_set):
                    # Update max_len if current subarray is longer
                    max_len = max(max_len, j - i + 1)
                    
        return max_len