class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        # Create a DP table initialized with negative infinity
        # dp[i][j] represents the max dot product using nums1[:i] and nums2[:j]
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 1. Calculate the product of the current pair
                current_prod = nums1[i-1] * nums2[j-1]
                
                # 2. Decide the best value for dp[i][j]
                dp[i][j] = max(
                    current_prod,                          # Start fresh with only this pair
                    current_prod + dp[i-1][j-1],           # Add this pair to best previous sub-problem
                    dp[i-1][j],                            # Skip the current element of nums1
                    dp[i][j-1]                             # Skip the current element of nums2
                )
                
        return dp[n][m]