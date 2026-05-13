from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        # diff array needs to go up to 2 * limit + 2 to safely handle index + 1 operations
        diff = [0] * (2 * limit + 2)
        
        # Process each pair
        for i in range(n // 2):
            A = min(nums[i], nums[n - 1 - i])
            B = max(nums[i], nums[n - 1 - i])
            
            # Apply the difference array boundaries
            diff[2] += 2
            diff[A + 1] -= 1
            diff[A + B] -= 1
            diff[A + B + 1] += 1
            diff[B + limit + 1] += 1
            
        min_moves = float('inf')
        current_moves = 0
        
        # Sweep through all possible target sums
        for T in range(2, 2 * limit + 1):
            # Accumulate the prefix sum to get the actual moves for target T
            current_moves += diff[T]
            # Track the minimum moves found so far
            min_moves = min(min_moves, current_moves)
            
        return min_moves