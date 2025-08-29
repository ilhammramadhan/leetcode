class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Step 1: Count the number of even and odd numbers in the range [1, n] for x.
        
        # Number of even values for x
        even_n = n // 2
        
        # Number of odd values for x
        odd_n = n - even_n  # Or (n + 1) // 2

        # Step 2: Count the number of even and odd numbers in the range [1, m] for y.
        
        # Number of even values for y
        even_m = m // 2
        
        # Number of odd values for y
        odd_m = m - even_m # Or (m + 1) // 2

        # Step 3: Calculate the total number of winning pairs for Alice.
        # This combines our two cases:
        # Case 1: x is odd AND y is even
        # Case 2: x is even AND y is odd
        
        # The number of pairs for Case 1 is (number of odd x's) * (number of even y's)
        odd_x_even_y_pairs = odd_n * even_m
        
        # The number of pairs for Case 2 is (number of even x's) * (number of odd y's)
        even_x_odd_y_pairs = even_n * odd_m
        
        # The total is the sum of the two cases.
        return odd_x_even_y_pairs + even_x_odd_y_pairs