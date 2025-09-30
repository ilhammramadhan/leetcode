from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # Continue the process as long as the list has more than one element.
        while len(nums) > 1:
            # Create a temporary list to store the results of the current iteration.
            new_nums = []
            # Iterate through the current list to calculate the new values.
            # We stop at the second to last element because we need pairs (nums[i], nums[i+1]).
            for i in range(len(nums) - 1):
                # Calculate the sum modulo 10 and add it to our new list.
                current_sum = (nums[i] + nums[i+1]) % 10
                new_nums.append(current_sum)
            
            # Replace the old list with the newly computed one for the next iteration.
            nums = new_nums
        
        # When the loop finishes, nums will have only one element. Return it.
        return nums[0]