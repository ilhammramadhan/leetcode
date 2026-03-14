class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Step 1: Check if k is out of bounds
        total_happy_strings = 3 * (2 ** (n - 1))
        if k > total_happy_strings:
            return ""
            
        self.count = 0
        self.result = ""
        
        # Step 2: Define the backtracking function
        def backtrack(current_string):
            # Base Case: The string has reached the desired length
            if len(current_string) == n:
                self.count += 1
                if self.count == k:
                    self.result = current_string
                return
            
            # Step 3: Try appending letters in alphabetical order
            for char in ['a', 'b', 'c']:
                # Only add if it's the first char OR different from the last char
                if not current_string or current_string[-1] != char:
                    backtrack(current_string + char)
                    
                    # Early exit: If we found our result deep in the recursion, stop searching
                    if self.result:
                        return
                        
        # Start the recursion with an empty string
        backtrack("")
        
        return self.result