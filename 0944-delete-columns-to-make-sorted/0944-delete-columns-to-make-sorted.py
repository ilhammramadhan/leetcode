class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete_count = 0
        
        # Number of rows (n) and number of columns (m)
        num_rows = len(strs)
        num_cols = len(strs[0])
        
        # Iterate through each column
        for c in range(num_cols):
            # Check characters in the column from top to bottom
            for r in range(num_rows - 1):
                # Compare current character with the one directly below it
                if strs[r][c] > strs[r + 1][c]:
                    # Not sorted lexicographically! 
                    delete_count += 1
                    break # Move to the next column immediately
        
        return delete_count