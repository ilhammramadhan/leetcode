class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # 1. Sort batteries to easily access the largest ones
        batteries.sort()
        
        # 2. Calculate the sum of all batteries
        total_power = sum(batteries)
        
        # 3. Iterate backwards from the largest battery
        # We check if the largest battery is 'too big' compared to the average.
        while batteries[-1] > total_power // n:
            # Pick the largest battery
            largest = batteries.pop()
            
            # This battery can cover one computer entirely for the final duration.
            # So we reduce the problem:
            # We now have n-1 computers to worry about.
            n -= 1
            
            # We remove the battery's power from the pool
            total_power -= largest
            
            # If we run out of extra batteries or reduce n to 0 (unlikely given constraints)
            if n == 0: return 0 

        # 4. Once the largest battery is <= average, 
        # it means all remaining batteries can be perfectly distributed as fluid.
        return total_power // n