class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        neg_count = 0
        min_abs_val = float('inf')
        
        for row in matrix:
            for val in row:
                # Add the absolute value to our sum
                total_sum += abs(val)
                
                # Keep track of the number of negatives
                if val < 0:
                    neg_count += 1
                
                # Keep track of the smallest absolute value
                if abs(val) < min_abs_val:
                    min_abs_val = abs(val)
        
        # If the number of negatives is even, they all cancel out
        if neg_count % 2 == 0:
            return total_sum
        
        # If odd, the smallest absolute value must remain negative
        return total_sum - 2 * min_abs_val