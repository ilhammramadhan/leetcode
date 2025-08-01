from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Step 1: Handle the edge case where numRows is 0.
        if numRows == 0:
            return []

        # Step 2: Initialize the triangle with the first row.
        triangle = [[1]]

        # Step 3: Loop to generate the remaining rows.
        # We already have one row, so we loop numRows - 1 times.
        for i in range(numRows - 1):
            # Get the last row from the triangle.
            previous_row = triangle[-1]
            
            # Start the new row with a 1.
            new_row = [1]
            
            # Calculate the middle elements by summing adjacent pairs
            # from the previous row.
            for j in range(len(previous_row) - 1):
                new_row.append(previous_row[j] + previous_row[j + 1])
            
            # End the new row with a 1.
            new_row.append(1)
            
            # Add the completed new row to the triangle.
            triangle.append(new_row)
            
        # Step 4: Return the completed triangle.
        return triangle