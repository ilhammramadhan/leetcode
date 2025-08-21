class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        Calculates the number of submatrices that have all ones.

        The logic iterates through the matrix row by row, maintaining an array `h`
        that stores the height of consecutive ones ending at the current cell in each column.
        For each cell, it then looks leftwards, calculating how many valid rectangles
        can be formed with this cell as the bottom-right corner.
        """
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        total_submatrices = 0
        # h stores the height of consecutive 1s ending at the current row for each column.
        h = [0] * n

        # Iterate through each row of the matrix.
        for i in range(m):
            # Step 1: Update the height array for the current row.
            for j in range(n):
                if mat[i][j] == 1:
                    h[j] += 1
                else:
                    h[j] = 0
            
            # Step 2: Count submatrices ending at the current row `i`.
            # For each cell (i, j), we count the number of submatrices with it
            # as the bottom-right corner.
            for j in range(n):
                # If height is 0, no rectangle can end here.
                if h[j] == 0:
                    continue
                
                # The minimum height of the rectangle as we expand it to the left.
                min_height = h[j]
                
                # Look left from column `j` to form rectangles of increasing width.
                for k in range(j, -1, -1):
                    # If we hit a column with 0 height, we can't expand further left.
                    if h[k] == 0:
                        break
                    
                    # The height of the rectangle is limited by the shortest column in it.
                    min_height = min(min_height, h[k])
                    
                    # For a given width (from k to j), we can form `min_height` rectangles
                    # of heights 1, 2, ..., min_height.
                    total_submatrices += min_height
                        
        return total_submatrices