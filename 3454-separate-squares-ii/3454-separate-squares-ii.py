from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # 1. Create a list of all y-boundaries
        y_events = set()
        for _, y, l in squares:
            y_events.add(y)
            y_events.add(y + l)
        
        sorted_y = sorted(list(y_events))
        y_map = {y: i for i, y in enumerate(sorted_y)}
        
        # 2. Assign x-intervals to each y-strip
        # strip_widths[i] will store the union of x-intervals for the strip (sorted_y[i], sorted_y[i+1])
        strips = [[] for _ in range(len(sorted_y) - 1)]
        for x, y, l in squares:
            for i in range(y_map[y], y_map[y + l]):
                strips[i].append((x, x + l))
        
        # 3. Calculate the total area and area per strip
        strip_data = [] # List of (y_low, y_high, union_width, strip_area)
        total_area = 0
        
        for i in range(len(sorted_y) - 1):
            if not strips[i]:
                continue
            
            # Merge x-intervals for this strip
            strips[i].sort()
            union_w = 0
            curr_s, curr_e = strips[i][0]
            for nxt_s, nxt_e in strips[i][1:]:
                if nxt_s < curr_e:
                    curr_e = max(curr_e, nxt_e)
                else:
                    union_w += curr_e - curr_s
                    curr_s, curr_e = nxt_s, nxt_e
            union_w += curr_e - curr_s
            
            height = sorted_y[i+1] - sorted_y[i]
            area = union_w * height
            strip_data.append((sorted_y[i], sorted_y[i+1], union_w, area))
            total_area += area
        
        # 4. Find the y-coordinate that splits the area
        target_half = total_area / 2
        accumulated_area = 0
        
        for y_low, y_high, width, area in strip_data:
            if accumulated_area + area >= target_half - 1e-9:
                # The dividing line is inside this strip
                needed_area = target_half - accumulated_area
                # Area = width * offset -> offset = Area / width
                return y_low + (needed_area / width)
            accumulated_area += area
            
        return float(sorted_y[-1])