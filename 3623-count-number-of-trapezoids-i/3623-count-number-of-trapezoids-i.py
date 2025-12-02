from typing import List
from collections import Counter

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # 1. Group points by their y-coordinate
        # We use a Counter to count how many points share the same y-value.
        # Key = y-coordinate, Value = number of points at that y.
        y_counts = Counter()
        for x, y in points:
            y_counts[y] += 1
            
        # 2. Calculate the number of ways to form a horizontal line (a pair of points)
        # for each unique y-coordinate.
        # If a row has 'k' points, we can choose 2 points in k*(k-1)/2 ways.
        ways_per_row = []
        for count in y_counts.values():
            if count >= 2:
                num_pairs = count * (count - 1) // 2
                ways_per_row.append(num_pairs)
        
        # If we don't have at least two rows with pairs, we can't form a trapezoid.
        if len(ways_per_row) < 2:
            return 0
            
        # 3. Calculate the sum of products of all pairs of rows efficiently.
        # We need: sum(ways[i] * ways[j]) for all i < j
        # Formula: Result = ((Sum of all ways)^2 - (Sum of each way squared)) / 2
        
        MOD = 10**9 + 7
        
        total_sum = sum(ways_per_row)
        sum_of_squares = sum(w * w for w in ways_per_row)
        
        # Calculate result using integer division
        result = (total_sum * total_sum - sum_of_squares) // 2
        
        return result % MOD