from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        # We need a small value (epsilon) to compare floating-point numbers.
        # Direct comparison like `if result == 24` can fail due to precision issues.
        EPSILON = 1e-6
        
        # Convert the input integers to floats to handle real division correctly.
        nums = [float(c) for c in cards]
        
        def solve(current_nums: List[float]) -> bool:
            """
            This is our recursive helper function.
            It returns True if the numbers in current_nums can make 24.
            """
            
            # 1. BASE CASE
            # If there's only one number left, check if it's 24.
            if len(current_nums) == 1:
                return abs(current_nums[0] - 24) < EPSILON

            # 2. RECURSIVE STEP
            # Iterate through all unique pairs of numbers (a, b) from the list.
            # Using `range(i + 1, ...)` ensures we don't pick the same pair twice (like (a,b) and (b,a)).
            for i in range(len(current_nums)):
                for j in range(i + 1, len(current_nums)):
                    a = current_nums[i]
                    b = current_nums[j]

                    # Create a list of the numbers that were NOT chosen for this operation.
                    remaining = [current_nums[k] for k in range(len(current_nums)) if k != i and k != j]
                    
                    # Generate all possible results from operating on a and b.
                    # For each result, create a new list and make a recursive call.
                    # If any call returns True, we've found a solution!
                    
                    # Operation: Addition
                    if solve(remaining + [a + b]): return True
                    # Operation: Multiplication
                    if solve(remaining + [a * b]): return True
                    # Operation: Subtraction (both ways)
                    if solve(remaining + [a - b]): return True
                    if solve(remaining + [b - a]): return True
                    # Operation: Division (both ways, checking for non-zero divisor)
                    if b != 0 and solve(remaining + [a / b]): return True
                    if a != 0 and solve(remaining + [b / a]): return True

            # If the loops complete, it means no combination of pairs and
            # operations from this `current_nums` list could form 24.
            return False

        # Start the recursion with the initial list of numbers.
        return solve(nums)