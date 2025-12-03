from math import gcd
from collections import defaultdict, Counter
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0
        
        # Key: (dy, dx) normalized slope
        # Value: List of tuples (intercept_identifier, length_squared)
        slopes = defaultdict(list)
        
        # 1. Generate all segments
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                dy = y2 - y1
                dx = x2 - x1
                
                # Normalize Slope
                g = gcd(dy, dx)
                dy //= g
                dx //= g
                
                # Standardize direction
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                
                # Line Intercept Identifier: dx*y - dy*x = c
                # This uniquely identifies the infinite line for this specific slope.
                c = dx * y1 - dy * x1
                
                # Length Squared
                length_sq = (x2 - x1)**2 + (y2 - y1)**2
                
                slopes[(dy, dx)].append((c, length_sq))
                
        total_trapezoids = 0
        total_parallelograms = 0
        
        # 2. Process each slope group
        for slope_key, segments in slopes.items():
            k = len(segments)
            if k < 2:
                continue
            
            # --- A. Count Valid Parallel Pairs (Trapezoid Base Logic) ---
            # Total pairs of segments with this slope
            pairs = k * (k - 1) // 2
            
            # Remove pairs that are Collinear (lying on the same infinite line c)
            # Group by intercept 'c'
            line_groups = defaultdict(list) 
            for c, length in segments:
                line_groups[c].append(length)
                
            for lengths in line_groups.values():
                m = len(lengths)
                if m > 1:
                    pairs -= m * (m - 1) // 2
            
            total_trapezoids += pairs
            
            # --- B. Count Parallelogram Candidates (Same Slope + Same Length) ---
            # We must also exclude collinear segments here!
            
            # Group by Length within this slope
            len_groups = defaultdict(list)
            for c, l_sq in segments:
                len_groups[l_sq].append(c)
            
            for l_sq, intercepts in len_groups.items():
                m = len(intercepts)
                if m < 2:
                    continue
                    
                # Pairs with same slope AND same length
                p_pairs = m * (m - 1) // 2
                
                # Subtract those that are collinear
                # (Same slope, same length, AND same line intercept)
                sub_line_counts = Counter(intercepts)
                for count in sub_line_counts.values():
                    p_pairs -= count * (count - 1) // 2
                
                total_parallelograms += p_pairs

        # 3. Final Correction
        # 'total_trapezoids' counts parallelograms twice (once for each parallel pair).
        # 'total_parallelograms' counts each parallelogram twice (detected at both slopes).
        # We want to count parallelograms exactly once.
        # Formula: (Trapezoids + 2*Parallelograms) - (2*Parallelograms / 2) = Trapezoids + Parallelograms
        
        return total_trapezoids - (total_parallelograms // 2)