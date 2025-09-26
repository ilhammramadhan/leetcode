import collections

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        # Step 1: Sort the array
        nums.sort()
        
        count = 0
        
        # Step 2: Iterate and use two pointers
        for i in range(n - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    # Since nums is sorted, all elements from left to right-1 
                    # will also form a valid triangle with nums[right] and nums[i]
                    count += (right - left)
                    right -= 1
                else:
                    # Sum is too small, need a larger value
                    left += 1
                    
        # Step 3: Return the count
        return count