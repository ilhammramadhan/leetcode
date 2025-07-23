class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # 1. Prioritize the higher-scoring pair
        if x < y:
            # If "ba" offers more points, we flip the problem.
            # We'll search for "ba" first by reversing the string and swapping the scores.
            return self.maximumGain(s[::-1], y, x)

        # At this point, x >= y, so we prioritize removing "ab"

        total_points = 0
        
        # 2. First Pass: Remove the higher-scoring pair ("ab")
        # We use a list as a stack to build a new string without "ab"s.
        stack_a = []
        for char in s:
            if char == 'b' and stack_a and stack_a[-1] == 'a':
                # Found an "ab" pair. Remove 'a' from the stack and add points.
                stack_a.pop()
                total_points += x
            else:
                # No "ab" pair found, just add the character to the stack.
                stack_a.append(char)

        # `stack_a` now contains the string after all "ab"s are removed.
        # Example: "cdbcbbaaabab" -> "cdbcbbaa" (after removing one "ab") -> "cdbcba" (after removing another) ...
        # The final result in stack_a would be ['c', 'd', 'b', 'c'] after all passes.
        
        # 3. Second Pass: Remove the lower-scoring pair ("ba") from the remaining string
        # We process the result from the first pass.
        stack_b = []
        for char in stack_a:
            if char == 'a' and stack_b and stack_b[-1] == 'b':
                # Found a "ba" pair. Remove 'b' from the stack and add points.
                stack_b.pop()
                total_points += y
            else:
                stack_b.append(char)

        # 4. Return the total accumulated points
        return total_points