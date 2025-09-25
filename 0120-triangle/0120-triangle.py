class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second-to-last row and iterate upwards
        for i in range(len(triangle) - 2, -1, -1):
            # Iterate through each element of the current row
            for j in range(len(triangle[i])):
                # Update the current element with the minimum path sum
                # from that element to the bottom of the triangle.
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        
        # The top element now contains the minimum path sum from top to bottom
        return triangle[0][0]