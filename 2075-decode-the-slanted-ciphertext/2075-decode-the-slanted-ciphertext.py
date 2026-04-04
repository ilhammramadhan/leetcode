class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Handle the edge case of an empty string
        if not encodedText:
            return ""
            
        cols = len(encodedText) // rows
        result = []
        
        # Iterate through each starting column of the first row
        for c in range(cols):
            # Move down the matrix diagonally
            for r in range(rows):
                curr_col = c + r
                
                # If the diagonal goes out of the right bounds of the matrix, stop
                if curr_col >= cols:
                    break
                
                # Calculate the 1D index mapping
                index = r * cols + curr_col
                result.append(encodedText[index])
                
        # Join the characters and remove any trailing padding spaces
        return "".join(result).rstrip()