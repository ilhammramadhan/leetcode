class Solution:
    def minPartitions(self, n: str) -> int:
        # Find the maximum character in the string 'n'
        # Since characters '0'-'9' are ordered sequentially in ASCII, 
        # max(n) will correctly return the largest digit as a string.
        max_digit_str = max(n)
        
        # Convert that string character back to an integer and return it
        return int(max_digit_str)