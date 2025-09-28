class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Step 1: Sort the array in ascending order.
        # This makes it easy to access the largest numbers.
        nums.sort()
        
        # Step 2: Iterate backward from the end of the array.
        # We need at least three sides, so the loop goes down to index 2.
        for i in range(len(nums) - 1, 1, -1):
            # The three potential sides are nums[i], nums[i-1], and nums[i-2].
            # Let a = nums[i-2], b = nums[i-1], c = nums[i].
            
            # Step 3: Check the Triangle Inequality Theorem.
            # Since the array is sorted, we only need to check if a + b > c.
            if nums[i-2] + nums[i-1] > nums[i]:
                # If the condition is met, we've found the largest possible perimeter.
                # Return the sum of the three sides.
                return nums[i-2] + nums[i-1] + nums[i]
        
        # Step 4: If the loop finishes, no valid triangle was found.
        return 0