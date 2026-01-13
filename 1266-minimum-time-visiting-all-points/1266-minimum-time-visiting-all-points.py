class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        
        # Iterate through the points, comparing current point to the next
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            
            # The time to move between two points is the maximum 
            # of the horizontal and vertical differences.
            total_time += max(abs(x2 - x1), abs(y2 - y1))
            
        return total_time