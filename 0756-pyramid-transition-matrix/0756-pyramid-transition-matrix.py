from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # 1. Map the allowed patterns for O(1) lookup
        # Key: bottom pair (e.g., 'BC'), Value: possible tops (e.g., {'C', 'F'})
        mapping = defaultdict(set)
        for pattern in allowed:
            mapping[pattern[:2]].add(pattern[2])
        
        # Memoization to avoid re-calculating the same row configurations
        memo = {}

        def solve(current_row, next_row):
            # Base Case: If current_row has only 1 block, we reached the top!
            if len(current_row) == 1:
                return True
            
            # If we finished building the next_row, move up to the next level
            if len(next_row) == len(current_row) - 1:
                return solve(next_row, "")
            
            # Check memo to see if we've tried building from this state before
            state = (current_row, next_row)
            if state in memo:
                return memo[state]
            
            # Logic to find the next block for the next_row
            # We look at the pair in current_row starting at the current index
            i = len(next_row)
            pair = current_row[i:i+2]
            
            if pair in mapping:
                for top in mapping[pair]:
                    # Try placing 'top' and recurse to build the rest of the row
                    if solve(current_row, next_row + top):
                        memo[state] = True
                        return True
            
            memo[state] = False
            return False

        return solve(bottom, "")