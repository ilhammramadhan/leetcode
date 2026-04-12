class Solution:
    def minimumDistance(self, word: str) -> int:
        # Helper to get (row, col) for a character
        def get_pos(char):
            idx = ord(char) - ord('A')
            return divmod(idx, 6)

        # Helper for Manhattan distance
        def dist(p1, p2):
            if p1 is None: return 0  # Initial position is free
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # Cache for memoization
        memo = {}

        def solve(idx, other_pos):
            # Base case: word completed
            if idx == len(word):
                return 0
            
            state = (idx, other_pos)
            if state in memo:
                return memo[state]
            
            curr_pos = get_pos(word[idx])
            prev_pos = get_pos(word[idx-1])
            
            # Option 1: Move the finger that just typed word[idx-1]
            cost1 = dist(prev_pos, curr_pos) + solve(idx + 1, other_pos)
            
            # Option 2: Move the "other" finger
            cost2 = dist(other_pos, curr_pos) + solve(idx + 1, prev_pos)
            
            res = min(cost1, cost2)
            memo[state] = res
            return res

        # Start at index 1. Finger 1 starts at word[0] (cost 0).
        # Finger 2 is currently "None" (waiting to be placed).
        return solve(1, None)