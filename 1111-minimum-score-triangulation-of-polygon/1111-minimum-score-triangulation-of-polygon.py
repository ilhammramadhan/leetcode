class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        
        # dp[i][j] will store the minimum score to triangulate
        # the polygon from vertex i to vertex j.
        dp = [[0] * n for _ in range(n)]

        # We iterate over the length of the polygon chain.
        # The smallest polygon has 3 vertices.
        for length in range(3, n + 1):
            
            # i is the starting vertex of the sub-polygon.
            for i in range(n - length + 1):
                # j is the ending vertex.
                j = i + length - 1
                
                # Initialize the score for this subproblem to a large value.
                dp[i][j] = float('inf')
                
                # k is the intermediate vertex that forms a triangle with i and j.
                # We try every possible k between i and j to find the minimum score.
                for k in range(i + 1, j):
                    
                    # This is the recurrence relation in action.
                    # Score = (min score of left sub-polygon) + 
                    #         (min score of right sub-polygon) + 
                    #         (score of the new triangle (i, k, j))
                    current_score = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    
                    # Update dp[i][j] with the minimum score found so far.
                    dp[i][j] = min(dp[i][j], current_score)

        # The final answer is the minimum score for the entire polygon (from vertex 0 to n-1).
        return dp[0][n-1]