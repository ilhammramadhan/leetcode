from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        # total_time will accumulate the cost of all balloons we remove.
        total_time = 0
        n = len(colors)
        
        # 'left' pointer marks the beginning of a consecutive group of same-colored balloons.
        left = 0
        
        while left < n:
            # These variables will track the data for the *current group*
            sum_of_group = 0
            max_of_group = 0
            
            # 'right' pointer scans forward to find the end of this group
            right = left
            
            # This inner loop finds the entire group of identical, consecutive colors
            while right < n and colors[right] == colors[left]:
                # Add the current balloon's time to the group's total
                sum_of_group += neededTime[right]
                
                # Keep track of the most expensive balloon in this group
                max_of_group = max(max_of_group, neededTime[right])
                
                # Move to the next balloon
                right += 1
            
            # Now, the group has ended (from 'left' to 'right - 1').
            # We must remove all balloons in this group *except* the most expensive one.
            # The cost of removals for this group is the group's total sum minus the one we keep.
            total_time += (sum_of_group - max_of_group)
            
            # The next group starts where this one ended.
            left = right
            
        return total_time