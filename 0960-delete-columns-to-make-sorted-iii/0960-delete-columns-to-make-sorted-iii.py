class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)       # Number of rows
        m = len(strs[0])    # Number of columns (length of each string)
        
        # dp[i] stores the length of the longest increasing subsequence
        # of columns ending at index i
        dp = [1] * m
        
        # Iterate through every column i (current column)
        for i in range(m):
            # Check every previous column j to see if we can extend the sequence
            for j in range(i):
                
                # Check if column j can precede column i for ALL rows
                can_extend = True
                for row in range(n):
                    if strs[row][j] > strs[row][i]:
                        can_extend = False
                        break
                
                # If valid for all rows, update dp[i]
                if can_extend:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The max value in dp is the max columns we can KEEP
        max_kept = max(dp)
        
        # The answer is total columns minus the ones we keep
        return m - max_kept