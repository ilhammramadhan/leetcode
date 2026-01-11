class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n_cols = len(matrix[0])
        heights = [0] * (n_cols + 1) # Extra 0 at the end to flush the stack
        max_area = 0
        
        for row in matrix:
            # Step 1: Update the histogram heights for the current row
            for i in range(n_cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # Step 2: Calculate largest rectangle in this row's histogram
            # We use a Monotonic Increasing Stack
            stack = [-1]
            for i in range(n_cols + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area