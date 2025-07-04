class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        """
        Finds the k-th character by working backward from the final string's state.

        This method avoids building the massive final string by tracing the
        k-th position back to its origin in the initial string "a". It iterates
        through the operations in reverse, at each step determining if the
        character was in the first or second half of the string. It keeps a
        running count of how many times the character's value was incremented
        due to a type 1 operation.
        """
        
        # 1. Initialization
        # Convert k to be 0-indexed for easier calculations.
        k -= 1
        
        # This will count how many times the character's value was shifted.
        num_increments = 0
        
        num_ops = len(operations)
        
        # 2. Iterate Backwards through the operations.
        for i in range(num_ops - 1, -1, -1):
            # The length of the string before operation 'i' was 2^i.
            # This serves as the midpoint for the string after operation 'i'.
            half_length = 2**i
            
            # 3. Check if k is in the second half and update accordingly.
            if k >= half_length:
                # Map k to its corresponding position in the first half.
                k -= half_length
                
                # If the operation was type 1, the second half was an
                # incremented copy, so we record the increment.
                if operations[i] == 1:
                    num_increments += 1
                    
        # 4. Calculate the final character.
        # The initial character is 'a'. We apply the collected increments.
        # We use modulo 26 because 'z' wraps around to 'a'.
        final_char_code = ord('a') + (num_increments % 26)
        
        return chr(final_char_code)