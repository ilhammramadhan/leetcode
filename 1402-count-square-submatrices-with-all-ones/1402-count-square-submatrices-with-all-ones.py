class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Get the dimensions of the matrix.
        rows = len(matrix)
        cols = len(matrix[0])
        
        # This variable will store the total sum of squares.
        total_squares = 0
        
        # Iterate through each cell of the matrix.
        for i in range(rows):
            for j in range(cols):
                # We only care about cells that are '1'.
                # The first row (i=0) and first col (j=0) are base cases;
                # they can only form 1x1 squares, so their values don't need to change.
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    # This is the core DP relation.
                    # The value at (i, j) becomes 1 plus the minimum of its 
                    # left, top, and top-left neighbors.
                    # This new value represents the side length of the largest
                    # square with this cell as its bottom-right corner.
                    matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                
                # The value at matrix[i][j] now represents the number of squares
                # that have this cell as their bottom-right corner.
                # We add this to our total count.
                total_squares += matrix[i][j]
                
        return total_squares