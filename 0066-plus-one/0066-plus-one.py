class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the end of the array (least significant digit)
        # range(start, stop, step)
        for i in range(len(digits) - 1, -1, -1):
            
            # If the current digit is less than 9, increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 (carrying the 1)
            digits[i] = 0
            
        # If the loop finishes, it means we had a carry-over 
        # for the most significant digit (e.g., [9, 9, 9] -> [0, 0, 0])
        # We need to add a 1 at the beginning.
        return [1] + digits