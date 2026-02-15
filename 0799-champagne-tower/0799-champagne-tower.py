class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Create a 102x102 grid filled with 0.0
        # We use 102 to ensure we don't go out of bounds when looking at the "next row"
        tower = [[0] * 102 for _ in range(102)]
        
        # Step 1: Pour everything into the top glass
        tower[0][0] = poured
        
        # Step 2: Loop through each row up to the target row
        for r in range(query_row):
            # Iterate through each glass in the current row 'r'
            # Row 'r' has exactly 'r + 1' glasses
            for c in range(r + 1):
                
                # Calculate the excess liquid in the current glass
                excess = (tower[r][c] - 1.0) / 2.0
                
                # If there is overflow, distribute it to the next row
                if excess > 0:
                    tower[r+1][c] += excess       # Bottom-left neighbor
                    tower[r+1][c+1] += excess     # Bottom-right neighbor
        
        # Step 3: Return the result, capped at 1.0
        return min(1.0, tower[query_row][query_glass])